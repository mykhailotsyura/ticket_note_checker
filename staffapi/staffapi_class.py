#!/usr/bin/python
from functions.common_functions import *
from modules import *


class staffapi:
    user=''

    def __init__(self):
        self.login()

    def get_user_loginstatus(self):
        return self.user.login_status
    def get_user_sessionid(self):
        return self.user.sessionid
    def get_user_credentials(self):
        return self.user.get_credentials()

    def login(self):
       self.user = staffapi_user()

    def ticket_search(self, ticket_id):
        post_data = { "sessionid": self.user.sessionid ,
                "query": ticket_id,
                "ticketid": 1 }
        req_url = defines.API_BASE_URL + defines.API_ENDPOINTS["tickets_search"]
        return post_request ( req_url, post_data ).encode('utf-8')
    
    def ticket_list (self, departmentid, statusid, ownerid = 0 , 
            wantticketdata = 0, wantattachmentdata = 0, sortby = "ticketid", 
            sortorder = "asc", start = 0, limit = 100):
        post_data = locals()
        post_data.pop('self')
        post_data['sessionid'] = self.get_user_sessionid()
        req_url = defines.API_BASE_URL + defines.API_ENDPOINTS['tickets_list']
        return post_request ( req_url, post_data ).encode('utf-8')
       
    def getinfo ( self, wantticketdata , wantmacros = 0, wantchatdata = 0,
            wantstaff = 0, wantavatars = 0 ):
        post_data = locals()
        post_data.pop('self')
        post_data['sessionid'] = self.get_user_sessionid()
        print(post_data)

        req_url = defines.API_BASE_URL + defines.API_ENDPOINTS['getinfo']
        return post_request ( req_url, post_data ).encode('utf-8')        

    

