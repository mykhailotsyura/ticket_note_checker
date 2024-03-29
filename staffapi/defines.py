#!/usr/bin/python
import os
from dotenv import load_dotenv

dotenv_path = '/root/techsup_notify/.env'
load_dotenv(dotenv_path)

kayako_username = os.getenv("kayako_username")
kayako_password = os.getenv("kayako_password")
# DIR_BASE = os.path.dirname(os.path.realpath(__file__)) + "/staffapi" ;
DIR_BASE = os.path.dirname(os.path.realpath(__file__))
DIR_TMP = os.path.join(DIR_BASE, "tmp")
# DIR_TMP = os.path.join ( DIR_BASE,"tmp");


# Update password here
API_LOGIN_DATA = {
    "username": kayako_username,
    "password": kayako_password}

API_BASE_URL = 'https://support.namecheap.com/staffapi/index.php?'

API_ENDPOINTS = {
    "login": "/Core/Default/Login",
    "getinfo": "/Core/Default/GetInfo",
    "tickets_search": "/Tickets/Retrieve/Search",
    "tickets_list": "Tickets/Retrieve"}

SESSION_FILE_NAME = "STAFFAPI_USER_SESSION"
SESSION_FILE_LOCATION = os.path.join(DIR_TMP, SESSION_FILE_NAME)
SESSION_FILE_FIELDS = ["sessid", "sesstimeout"]

SESSIONID = str()
