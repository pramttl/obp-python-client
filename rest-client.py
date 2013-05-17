'''
Client to access data using the REST API provided by the Openbank Project, Social Finance Application.
If Authorization is required to access a resource then the client makes use of the OAUTH_HEADER_FILE generated
by the get_oauth_headers.py program.
'''

from settings import *

#--This is the location from where a client application gets user resources from.
API_LOCATION = 'https://demo.openbankproject.com/sandbox/obp/v1.1'
OAUTH_HEADER_FILE = 'saved_oauth_header.txt'

# These settings overwrite the defaults above.
from settings import *

import requests
import pickle
import sys
import simplejson as json
from pprint import pprint
from urlparse import urljoin

DEFAULT = False

try:
    resource_url = API_LOCATION + sys.argv[1]
    print "Fetching data from the following endpoint:\n"
    print resource_url
except IndexError:
    print "Fetching data from the root API endpoint"
    resource_url = API_LOCATION

# Loading the OAuth Header object from the file where it was saved.
f= open(OAUTH_HEADER_FILE, 'r') 
oauth = pickle.load(f)

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

