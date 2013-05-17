# settings.py

''' urljoin joins urls carefully so that you do not have to worry about the extreme forward slashes you put'''
from urlparse import urljoin

############################# USER DEFINED SETTINGS - Start Here ####################################
'''
Most Credentials have been already set to use the Open Bank Project well.
You just need
'''

#TODO: Add explaination on how to set the below OAuth Specific Settings for a general OAuth 1.0 Application.

## OAUTH SERVER PROVIDER PARAMETERS
OAUTH_BASE_URL = 'https://demo.openbankproject.com/'
CONSUMER_KEY =  'gqnb4xtazkbb0ij0xynylc4qa3z0jj1n4bo5qww5'   #***** PLEASE USE YOUR CONSUMER CREDENTIALS ******
CONSUMER_SECRET = '3yif1c5gpollqp4q2gioe2ueftti0za13tnupcvd' #***** PLEASE USE YOUR CONSUMER CREDENTIALS ******

#*** Remove /sandbox in production ***
REQUEST_TOKEN_URL = urljoin(OAUTH_BASE_URL,'/sandbox/oauth/initiate')
OAUTH_CALLBACK = 'oob'
AUTHORIZE_URL_BASE = urljoin(OAUTH_BASE_URL,'/sandbox/oauth/authorize?oauth_token=')
ACCESS_TOKEN_URL = urljoin(OAUTH_BASE_URL, '/sandbox/oauth/token')

# API PARAMETERS
API_LOCATION = 'https://demo.openbankproject.com/sandbox/obp/v1.1' # Absolute location of the API.


# (Optional Parameters - These parameters have a default defined already in the main application.)
OAUTH_HEADER_FILE = 'saved_oauth_header.txt'

