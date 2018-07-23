#!/usr/bin/env python
# -*- coding utf8 -*-

# from weibo import APIClient
import weibo as wb
import urllib2
import urllib
import sys
import time
from time import clock
import csv
import random

reload(sys)
sys.setdefaultencoding('utf-8')

''' Step 0 Login With OAuth2.0'''
if __name__ == "__main__":
    APP_KEY = '1370570361' # app key
    APP_SECRET = 'e2eff2e0774437c099399d64a2c57562' # app secret
    CALLBACK_URL = 'https://github.com/Zanyy2k' # set callback url exactly like this!
    AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
    USERID = 'yuzongdongsg@hotmail.com' #your weibo user id
    PASSWD = 'Wolf1234!' #your pw

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    referer_url = client.get_authorize_url()
    print "referer url is : %s" % referer_url

    cookies = urllib2.HTTPCookieProcessor()
    