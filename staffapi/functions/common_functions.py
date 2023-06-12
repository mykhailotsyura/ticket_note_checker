#!/usr/bin/python
from .. import defines
import xml.etree.ElementTree as ET                                                          
import requests as req
from xml.dom import minidom

def post_request ( request_url , request_data, headers = {} ):
    req_handler = req.post ( request_url, data = request_data, headers = headers );
    if req_handler.status_code == 200:
        return req_handler.text
    else:
        raise Exception ({ 'URL':req_handler.url , 'HTTP_CODE':req_handler.status_code})

def get_request ( request_url , auth = None ):
    if auth == None:
        req_handler = req.get ( request_url );
    elif isinstance ( auth, dict ) :
        req_handler = req.get ( request_url, 
                auth = (auth['username'],auth['password'] ))
    else:
        raise Exception ("Function '" + __name__ + "' : auth variable should be 'dict'" )
    if req_handler.status_code == 200:
        return req_handler
    else:
        raise Exception ({ 'URL':req_handler.url , 'HTTP_CODE':req_handler.status_code})


def parse_xml( xml_data ):
    root = ET.fromstring ( xml_data );
    members = dict();
    for child in root:
        members [ child.tag ] = child.text;
    return members ;

    
def check_session():
    #TO DO
    print ''

import sys
def save_session( session_dict, save_path = defines.SESSION_FILE_LOCATION ):
    
    root = ET.Element("sess");
    for key in session_dict:
        sub = ET.SubElement (root, key);
        sub.text = str ( session_dict[key] );
    
    xmlstr = minidom.parseString ( ET.tostring (root) ).toprettyxml();
    
    f = open(save_path, "w+");
    f.write ( xmlstr );
    f.close();
