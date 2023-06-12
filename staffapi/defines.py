#!/usr/bin/python
import os
#DIR_BASE = os.path.dirname(os.path.realpath(__file__)) + "/staffapi" ;
DIR_BASE = os.path.dirname(os.path.realpath(__file__)) ;
DIR_TMP = os.path.join ( DIR_BASE, "tmp");
#DIR_TMP = os.path.join ( DIR_BASE,"tmp");


### Update password here
API_LOGIN_DATA={
        "username": "USERNAME",
        "password": "PASSWORD"};

API_BASE_URL="https://internal.namecheap.com/staffapi/index.php?";

API_ENDPOINTS={
        "login":"/Core/Default/Login",
        "getinfo":"/Core/Default/GetInfo",
        "tickets_search":"/Tickets/Retrieve/Search",
        "tickets_list": "Tickets/Retrieve"};

SESSION_FILE_NAME= "STAFFAPI_USER_SESSION";
SESSION_FILE_LOCATION= os.path.join ( DIR_TMP, SESSION_FILE_NAME);
SESSION_FILE_FIELDS= ["sessid","sesstimeout"]

SESSIONID=str();
