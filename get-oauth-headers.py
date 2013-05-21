'''
Code to obtain the OAuth Authorization Headers from an OAuth provider 
(Openbank Project is the OAuth provider in this demo)
'''

from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
import pickle
from urlparse import parse_qs

OAUTH_HEADER_FILE = 'saved_oauth_header.txt'

## OAUTH SERVER PROVIDER PARAMETERS
from settings import *
''' 
** All the Settings should be correctly defined in settings.py file **
(Any settings defined before the above line in this file itself are overwritten)
'''

# useful alias' to the above parameters
client_key = CONSUMER_KEY
client_secret = CONSUMER_SECRET

print "******** GETTING OAUTH HEADERS AND DUMPING INTO TEXT FILE *************"
#print AUTHORIZE_URL_BASE

oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET,callback_uri=OAUTH_CALLBACK)
r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)

credentials = parse_qs(r.content)
oauth_token = credentials.get('oauth_token')[0]
oauth_token_secret = credentials.get('oauth_token_secret')[0]
oauth_callback_confirmed = credentials.get('oauth_callback_confirmed')[0]

if oauth_callback_confirmed:
    print "OAuth Callback has been Confirmed, Verification Remaining...."

# Eg. oauth_token = 5L2IJZIS4NP1MMSC311YL5OHGRICLDPBUJT4W1L4
# Eg. oauth_token_secret = H42EI1CEPH4RLILA5GSRTJ4GYVRRU4CXAGBFAFAF

# This parameter is mostly true if the request succeeds.
oauth_callback_confirmed = credentials.get('oauth_callback_confirmed')

authorize_url = AUTHORIZE_URL_BASE + oauth_token


# (Optional) For automatic opening of browser and entering Sandbox Credentials.
#-----------------------------------------------------------------------------------
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    print "Do you want an automatic sandbox demonstration? (y/n)"
    answer = raw_input()
    if answer == 'y' or answer == 'Y':
        print "Okay!! Gotcha, opening Firefox browser and doing the required stuff for you..."
        driver = webdriver.Firefox()
        driver.get(authorize_url)
        elem = driver.find_element_by_name("username")
        elem.send_keys("joe.bloggs@example.com")
        elem = driver.find_element_by_name("password")
        elem.send_keys("qwerty")
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_id("verify-code")
        verifier = elem.text
    else:
        raise
#-----------------------------------------------------------------------------------
except:
    print '------------------------------------------------------------------------'
    print 'Please VISIT this page to grant resource authorization:\n', authorize_url
    print '------------------------------------------------------------------------'
    print 'For Sandbox: login: joe.bloggs@example.com, password: qwerty'
    print '                                                                        '
    verifier = raw_input('Please input the verification code you see in your browser when you visit the above page:\n')

# Constructing an OAuth authorization Header object for the above user.
oauth = OAuth1(CONSUMER_KEY,
               client_secret=CONSUMER_SECRET,
               resource_owner_key=oauth_token,
               resource_owner_secret=oauth_token_secret,
               verifier=verifier)

r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
credentials = parse_qs(r.content)
access_token = credentials.get('oauth_token')[0]
token_secret = credentials.get('oauth_token_secret')[0]

oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=access_token,
                   resource_owner_secret=token_secret)

# Pickling the OAuth header object for the current user and storing it in a file.
f = open(OAUTH_HEADER_FILE, 'w') 
pickle.dump(oauth, f) 

'''
Note: Ideally one oauth header object maps to one user, so the object should be stored in a database instead for each user using such an OAuth client.
Since this is for demo purposes and we are having only one user - joe.bloggs@example.com, thus its okay to store the object once.
'''

print "OAuth Headers Successfully Created and saved. For the reference the OAuth token is:\n" + oauth_token
