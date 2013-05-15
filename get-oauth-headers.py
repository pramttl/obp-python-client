'''
Code to obtain the OAuth Authorization Headers from an OAuth provider 
(Openbank Project is the OAuth provider in this demo)
'''

from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
import pickle

## OAUTH SERVER PROVIDER PARAMETERS
BASE_URL = 'https://demo.openbankproject.com/sandbox'
CONSUMER_KEY = 'kdyftv5rwa33zont3qeb40zyqalacvhrt2e1tr1c'
CONSUMER_SECRET = 'yhqhizobp2vo42tdnjulekgd40lc4sja3jwm3j2j'
REQUEST_TOKEN_URL = BASE_URL + '/oauth/initiate'
OAUTH_CALLBACK = 'oob'
AUTHORIZE_URL_BASE = BASE_URL + '/oauth/authorize?oauth_token='
ACCESS_TOKEN_URL = BASE_URL + '/oauth/token'

# useful alias' to the above parameters
client_key = CONSUMER_KEY
client_secret = CONSUMER_SECRET

oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET,callback_uri=OAUTH_CALLBACK)
r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)

from urlparse import parse_qs
credentials = parse_qs(r.content)
oauth_token = credentials.get('oauth_token')[0]
oauth_token_secret = credentials.get('oauth_token_secret')[0]

# Eg. oauth_token = 5L2IJZIS4NP1MMSC311YL5OHGRICLDPBUJT4W1L4
# Eg. oauth_token_secret = H42EI1CEPH4RLILA5GSRTJ4GYVRRU4CXAGBFAFAF

# This parameter is mostly true if the request succeeds.
oauth_callback_confirmed = credentials.get('oauth_callback_confirmed')

authorize_url = AUTHORIZE_URL_BASE + oauth_token

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

# Pickling the OAuth header object for the current user and storing it in a file.
f = open('saved_oauth_header.txt', 'w') 
pickle.dump(oauth, f) 

'''
Note: Ideally one oauth header object maps to one user, so the object should be stored in a database instead for each user using such an OAuth client.
Since this is for demo purposes and we are having only one user - joe.bloggs@example.com, thus its okay to store the object once.
'''
