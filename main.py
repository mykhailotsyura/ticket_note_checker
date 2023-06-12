#!/usr/bin/python
#
import os,sys,re,json,traceback,random,time
import xml.etree.ElementTree as ET
import requests as req
#
from xml.dom import minidom
from flockos import Attachment,Views,HtmlView
from emoji_list import emoji_list
from staffapi.defines import *
from staffapi.staffapi_class import *
from staffapi.functions.common_functions import *
#

ENV = 'production'
#ENV = 'testing'
br = '<br>'
row_height = 35

#
# Basic HTML functions
#
def html_link ( text, href, target='_blank' ):
    a = ET.Element('a')
    a.text = text
    a.attrib['href'] = href
    a.attrib['target'] = target
    return ET.tostring(a)

def html_common_element (tag ,text, attrib = None, style = None ):
    a = ET.Element(tag)
    a.text = text
    if attrib:
        a.attrib[attrib[0]] = attrib[1]
    if style:
        a.attrib['style'] = style 
    return ET.tostring(a)

# 
# XML funct
#

def xml_to_ticketslist(xml_data):
    root = ET.fromstring ( xml_data )
    return root.findall("./tickets/ticket")
#
# Kayako Tickets functions
#
def find_notask_tickets ( xml_data ):
    keys_pattern = '|'.join (jira_keys)
    print jira_keys
    print keys_pattern
    tickets = xml_to_ticketslist ( xml_data )
    result = []
    for ticket in tickets:
        found=0
        for note in ticket.findall("./note"):
            jira_search_res = re.search("https?:\/\/"+jira_host+"\/browse\/(" + keys_pattern + ")-[0-9]{3,8}", note.text)
            trello_search_res =  re.search ("https?:\/\/" + trello_host + "\/?[0-9a-zA-Z\/-]*", note.text )
            if jira_search_res or trello_search_res :
                found=1
        if found == 0:
            result.append ( ticket )
    return result

def search_tickets ( xml_data, with_task = True ):
    tickets = xml_to_ticketslist ( xml_data )
    result = []
    for ticket in tickets:
        found=0
        for note in ticket.findall("./note"):
            re_res = re.search("https?:\/\/"+jira_host+"\/browse\/(CF|EASYWP)-[0-9]{3,8}", note.text)
            if ( re_res and with_task ) or not ( re_res and with_task ) :
                found=1
        if found == 0:
            result.append ( ticket )
    return result

#
# Jira tasks functions
#

def jira_gettask_bystatus ( json_data, task_status ):
    if task_status in jira_task_statuses:
        res = []
        is_not = task_status.find ('not_')
        if is_not == -1 :
            task_status = task_status.capitalize()
            not_cond = False
        elif is_not == 0 :
            task_status = task_status.partition('_')[2]
            not_cond = True
        else:
            raise Exception ('Something wrong happended, (shrug) | is_not ==' + str( is_not ) )
        for issue in json_data['issues']:
            fields = issue['fields']
            if ( fields['status']['name'] != task_status and not_cond ) or ( fields['status']['name'] != task_status and not not_cond ) :
                if not re.search ('EASYWP' ,issue['key']):
                    res.append ( {'key':issue['key'], 'created':fields['created'], 
                        'summary':fields['summary'], 'status':fields['status']['name']} )
    else:
        raise Exception('Task status "' + task_status + '" not in ', jira_task_statuses)
    return res


# #
# # OLD VERSION !!!
# def jira_search ( text ):
#     query = 'text~"' + text + '"'
#     url = 'https://' + jira_host + jira_api['base_url'] + jira_api['search'] + query
#     print ( url )
#     res = get_request( url, {'username':'xxxxxx', 'password':'xxxxxxx'})
#     json_data = res.json()
#     print  'Total: ',json_data['total']
#     res = []
#     if json_data['total'] >= 1:
#         res = []
#         for issue in json_data['issues']:
#             fields = issue['fields']
#             if fields['status']['name'] != 'Closed' and not re.search ('EASYWP' ,issue['key']):
#                res.append ( {'key':issue['key'], 'created':fields['created'], 
#                     'summary':fields['summary'], 'status':fields['status']['name']} )
#     else:
#         return False
#     return res

def jira_search_test ( search_url , text, login_credentials, processor_function, task_status ):
    query = 'text~"' + text + '"'
    search_url += query
    print ( search_url )
    res = get_request( search_url, login_credentials )
    json_data = res.json()
    print  'Total: ',json_data['total']
    if json_data['total'] >= 1:
        return processor_function(json_data, task_status)
    else:
        return False


#def jira_active_tasks ( json_data ):
#    res = []
#    for issue in json_data['issues']:
#        fields = issue['fields']
#        if fields['status']['name'] != 'Closed' and not re.search ('EASYWP' ,issue['key']):
#            res.append ( {'key':issue['key'], 'created':fields['created'], 
#                'summary':fields['summary'], 'status':fields['status']['name']} )
#    return res
    
#
# Return concatenated Jira task URL by a card ID
#

def get_card_url ( card_id ):
    return "https://" + jira_host + "/browse/" + card_id 

#
# Main searching function
#

def dpt_search_tickets (staffapi_obj, department_id, status_id, test_run = None ):
    
    if department_id == 44:
        service_name = "Jira/Trello: "
    else:
        service_name = "Jira: "
    
    for key,val in kayako_departments.items():
        if val == department_id:
            department_name = key
    for key,val in status_ids.items():
        if val == status_id:
            department_status = key
    start_message = "Checking " + department_name + " -- " + department_status
    start_message = "<b>" + start_message + "</b>"
    #flock_send_html ( start_message ) 
    flock_send_flockml ( start_message ) 

#    staffapi_obj = staffapi()
    
    tickets_list = staffapi_obj.ticket_list( department_id, status_id, limit = 1000, sortby = "lastactivity", wantticketdata = 1 )
    if test_run:
        notask_tickets = ET.fromstring(tickets_list).findall('./tickets/ticket')
    else:
        notask_tickets = find_notask_tickets ( tickets_list ) 
    
    print notask_tickets
    if len ( notask_tickets ) >= 1:
        found = True
        for elem in notask_tickets:
            html_data = []
            ticket_id = elem.attrib['id']
            ticket = elem.find('displayid').text
            html_hyperlink = html_link ( ticket ,kayako_url['ticket_view'] + ticket_id )
            html_data.append ( html_common_element ('b','Kayako: ') + html_hyperlink )
            print ticket
            #jira_res = jira_search ( ticket )
            jira_res = jira_search_test ( jira_url['search'], ticket, 
                    jira_login_credentials, jira_gettask_bystatus, 'not_closed' )
            print "Jira_res = ",jira_res
            if jira_res:
                for i,res_elem in enumerate (jira_res):
                    i = 0
                    for key,val in res_elem.items():
                        if i == 0:
                            key = html_common_element ('b', "Jira: " ) + key
                            i += 1
                        if key == "key":
                            val = html_link ( val, get_card_url(val) )
                        html_data.append ( key + ": " + val)
            else:
                html_data.append ( html_common_element ('b', service_name ) + "No active cards found by the ticket ID" )
            height = len (html_data) * 25
            print "HTML_DATA = ",html_data
            print "HEIGHT = ",height
            html_data = br.join(html_data)
            #flock_send_html ( html_data, height = height, color = colors['intermediate'])
            flock_send_flockml ( html_data, color = colors['intermediate'])
    else:
        found = False
    total_tickets = len( ET.fromstring ( tickets_list).findall('./tickets/ticket') )
    html_data = "Tickets in total in " + department_name + " " + department_status + ": " + str(total_tickets)
    if found:
        color = colors['end']['found']
    else:
        color = colors['end']['not_found']
	html_data = "No tickets found! | " + html_data
    html_data = html_common_element ( 'u' , html_data )
    #flock_send_html(html_data, color = color)
    flock_send_flockml (html_data, color = color)

    print 'total: ',total_tickets 

def flock_send_flockml_html (html_data, flockml_data, html_height = row_height, html_width = 800, color = None):
    
    views = Views()
    views.flockml = (flockml_data)
    views.html = HtmlView (inline=html_data, height=html_height, width=html_width)
    if color:
        attachment = Attachment ( views=views, color=color)
    else:
        attachment = Attachment( views=views )

    attachment = { "attachments": [ attachment.to_dict() ]}
    print json.dumps ( attachment, indent = 5 )
    headers = { 'Content-Type' : 'application/json' }
    print post_request ( webhook_url, json.dumps ( attachment ), headers )

def flock_send_html ( html_data, height = row_height, width = 800, color = None, send = True ):
    views = Views()
    views.html = HtmlView(inline=html_data,height=height,width=width)
    if color:
        attachment = Attachment ( views=views, color=color)
    else:
        attachment = Attachment( views=views )
    
    if send:
        attachment = { "attachments": [ attachment.to_dict() ]}
        print json.dumps ( attachment, indent = 5 )
        headers = { 'Content-Type' : 'application/json' }
        post_request ( webhook_url, json.dumps ( attachment ), headers )
    else:
        return attachment

def flock_send_flockml (flockml_data, send = True, color = None):
    views = Views()
    views.flockml = (flockml_data)
    if color:
        attachment = Attachment ( views=views, color = color )
    else:
        attachment = Attachment ( views=views )
    if send:
        attachment = { "attachments": [ attachment.to_dict() ]}
        print json.dumps ( attachment, indent = 5 )
        headers = { 'Content-Type' : 'application/json' }
        print post_request ( webhook_url, json.dumps ( attachment ), headers )
    else:
        return attachment

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def emojilist_toarray (filename):
    f_h = open ( filename, 'r')
    flen = file_len (filename)
    tmp_arr = []
    for i,line in enumerate ( f_h ):
        line = line.replace('\n','')
        if i == 0:
            line = "[ '" + line + "',"
        elif i == flen-1 :
            line = "'" + line + "']"
        else:
            line =  "'" + line + "',"
        tmp_arr.append (line)
        if i%10 == 0 and i != 0 :
            print ''.join (tmp_arr)
            tmp_arr = []
    
def get_random_emoji (emoji_list):
    rand_num = random.randrange ( 0, len ( emoji_list ))
    return emoji_list[rand_num]

colors = {
            'boop': '#f2b9dc',
            'wait': '#faa646',
            'error': '#D32424',
            'start': '#6DD4F0', 
            'intermediate': '#982ABB', 
            'end':
            {
                'found': '#D87E1E',
                'not_found': '#3FD2D6'
            }
        }

kayako_url = {'base':'https://support.namecheap.com/staff/index.php?'}
kayako_url['ticket_view'] = kayako_url['base'] + '/Tickets/Ticket/View/' 
kayako_departments = { 
    "EasyWP": 140, 
    "Hosting_Support": 24,
    "PE": 44,
    "CDN": 273
     }
status_ids = { 
    "escalated": 80, "awaiting_staff_response": 4
    }
jira_host = 'track.namecheap.net'
jira_api = {
    'base_url':'/rest/api', 
    'search':'/2/search?jql='
    }
jira_url = {
    'search': 'https://' + jira_host + 
    jira_api['base_url'] + jira_api['search']
    }
webhook_urls = {
    'production':'https://api.flock.com/hooks/sendMessage/4c2149a7-c11b-4230-b6f2-638c0e19c73c',
    'testing':'https://api.flock.com/hooks/sendMessage/dad648c6-11ff-4686-9423-9cf90badab09'
}
jira_task_statuses = ['active','not_closed','closed']
jira_login_credentials = {'username':'USERNAME', 'password':'PASSWORD'}

trello_host = "trello.com"

error_min_height = 135
webhook_url = webhook_urls[ENV]

jira_keys = ('CF','EASYWP','PE','TO','ASP','NCPPE','PHWS', 'DVLS')

try:
    
    staffapi_obj = staffapi()
    
    dpt_search_tickets ( staffapi_obj ,kayako_departments ["EasyWP"], status_ids ["escalated"], test_run = False )
    time.sleep (5)
    
    #wait = html_common_element ('sub', ' wait for it')
 #   flock_send_flockml ( wait, color = colors['wait'])
    #flock_send_html ( wait, color = colors['wait'], height = 40 )
    time.sleep (5)

 #   emoji = get_random_emoji(emoji_list)
 #   flock_send_flockml ( html_common_element ('i', 'Boop ') + emoji, color = colors ['boop'] )
    dpt_search_tickets ( staffapi_obj ,kayako_departments ["PE"], status_ids ["escalated"], test_run = False )

    time.sleep (5)
    dpt_search_tickets ( staffapi_obj ,kayako_departments ["Hosting_Support"], status_ids ["escalated"], test_run = False )
    
    time.sleep (5)
    dpt_search_tickets ( staffapi_obj ,kayako_departments ["CDN"], status_ids ["escalated"], test_run = False )

except:
    print 'Caught Error '
    excinfo = sys.exc_info()
    for key in excinfo:
        if isinstance ( key, traceback.types.TracebackType ):
            trace = traceback.format_tb(key)

    trace = trace.__str__().replace('\\n',br)
    n_newline = trace.count(br)
    print "N_newline = ",n_newline
    html_data = html_common_element ( 'font', 
            "Caught Error: " + excinfo[1].__str__(), 
            attrib = ('color','red'), style = "font-weight:bold;" )
    html_data +=  br + trace
    height = n_newline*row_height/3
    if height <= error_min_height:
        height = error_min_height
    flock_send_html ( html_data , height = height, color = colors['error'])
