'''
Client to access data using the REST API provided by the Openbank Project, Social Finance Application.
If Authorization is required to access a resource then the client makes use of the OAUTH_HEADER_FILE generated
by the get_oauth_headers.py program.
'''

#--This is the location from where a client application gets user resources from.
API_LOCATION = 'https://socialfinance.openbankproject.com/obp/v1.1'
OAUTH_HEADER_FILE = 'saved_oauth_header.txt'

import requests
import pickle
import sys
import simplejson as json
from pprint import pprint

DEFAULT = False

try:
    print "Fetching data from the following endpoint: " + sys.argv[1] + "\n"
except IndexError:
    print "Fetching data from the root API endpoint"
    DEFAULT = True

f= open(OAUTH_HEADER_FILE, 'r') 
oauth = pickle.load(f) 

# Example Resource Location. (List of all the banks)
if DEFAULT:
    resource_url = API_LOCATION
else:
    resource_url = API_LOCATION + sys.argv[1]

r = requests.get(url=resource_url, auth=oauth)

try:
    #Converting the obtained content into a useful python object.
    content = json.loads(r.content)
    JSON_ERROR = False
except json.decoder.JSONDecodeError:
    JSON_ERROR = True
    content = r.content

# Printing the accessed content on the terminal.
pprint(content)

