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
f= open(OAUTH_HEADER_FILE, 'r') 
oauth = pickle.load(f) 


# Example Resource Location. (List of all the banks)
resource_url = API_LOCATION + '/banks'

#TODO: Add more resource location examples.

r = requests.get(url=resource_url, auth=oauth)
content = r.content

# Printing the accessed content on the terminal.
print content


#TODO: Converting the obtained content into a useful python object.
