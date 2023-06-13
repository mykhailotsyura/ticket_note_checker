#!/usr/bin/python
#StaffAPI user class definition
#
import base64

#
from functions.common_functions import *


class staffapi_user:
    login_status = bool()
    login_credentials = dict()
    login_sessionid = str()

    ###
    def __init__(self, login_credentials = defines.API_LOGIN_DATA ):
        # TO DO: Check if user is already logged in
        # It is necessary to create a simple cookies mechanism 
        self.login_status = False
        if not self.login_status:
            login_handler = self.login( login_credentials )
            if login_handler:
                login_credentials['username'] = base64.b64encode ( login_credentials['username'])
                login_credentials['password'] = base64.b64encode ( login_credentials['password'])
                self.login_status = True
                self.login_credentials = login_credentials
                self.sessionid = login_handler['sessionid']
                save_session(login_handler)

            else:
                self.login_status = False
###
    def get_credentials (self):
        login_credentials = self.login_credentials
        login_credentials['username'] = base64.b64decode ( login_credentials['username'])
        login_credentials['password'] = base64.b64decode ( login_credentials['password'])
        return login_credentials

    def request_login ( self, login_credentials ) :
        req_url = defines.API_BASE_URL + defines.API_ENDPOINTS['login']
        req_result = post_request ( req_url, login_credentials )
        return parse_xml ( req_result )

    def login( self, login_credentials = defines.API_LOGIN_DATA ):
        #print 'In main: ',login_credentials
        child_dictionary = self.request_login( login_credentials )

        if child_dictionary['status'] == '-1':
            raise Exception ( child_dictionary )
            return False
        elif child_dictionary['status'] == '1':
            return child_dictionary
        else:
            raise Exception ('Can\'t determine whether log in has been successful')
            return False
