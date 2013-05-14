from __future__ import unicode_literals

'''
OAUTH SERVER PROVIDER PARAMETERS
'''
BASE_URL = 'https://demo.openbankproject.com/sandbox'
CONSUMER_KEY = 'kdyftv5rwa33zont3qeb40zyqalacvhrt2e1tr1c'
CONSUMER_SECRET = 'yhqhizobp2vo42tdnjulekgd40lc4sja3jwm3j2j'
REQUEST_TOKEN_URL = BASE_URL + 'oauth/initiate'
OAUTH_CALLBACK = 'oob'
AUTHORIZE_URL_BASE = BASE_URL + '/oauth/authorize?oauth_token='
ACCESS_TOKEN_URL = BASE_URL + '/oauth/token'

# useful alias' to the above parameters
client_key = CONSUMER_KEY
client_secret = CONSUMER_SECRET


import requests
from requests_oauthlib import OAuth1

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

print 'Please visit this page to grant resource authorization,', authorize_url

'''
# For the Sandbox environment in Open Bank Project, the test credentials are:
login: joe.bloggs@example.com 
password: qwerty
# Example Verification_Code = 08303
'''

verifier = raw_input('Please input the verifier:\n')


oauth = OAuth1(CONSUMER_KEY,
               client_secret=CONSUMER_SECRET,
               resource_owner_key=oauth_token,
               resource_owner_secret=oauth_token_secret,
               verifier=verifier)


'''
REST API (SERVER) PARAMETERS
'''

# This is the location from where a client application gets user resources from.
API_LOCATION = 'https://socialfinance.openbankproject.com/obp/v1.1'

##TODO
## Now we may use the REST API to access user resources.
#resource_url = API_LOCATION
#r = requests.get(url=url, auth=oauth)

