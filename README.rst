Openbank Project OAuth & REST Client
====================================

This code provides a sample OAuth 1.0 Python client, used to connect to 
the Openbank Project API. Although examples are created specifically for 
the Openbankproject, but the code can be suitably tweaked for any OAuth 1.0 provider.

The other objective is to be able to access Openbank Data via a REST Client, that uses the OAuth Headers / Token.
This part of the code has been added to the REST Client explained ahead.

OAuth_Authentication + API_Consumption

Thus the 2 aspects involved are:

[1] Getting the OAuth Token/Headers via the OBP OAuth Provider. (get-oauth-headers.py)
[2] Using the Rest API to get data from the Open Bank Project, Demo Application Server. (rest-client.py)

All the inital settings are defined in the "settings.py" file.

Getting Access Token via OBP OAuth Provider.
----------------------------------------------------------------------------
This has been inllustrated in the get-oauth-headers.py
The code gets the access token authorizes it, constructs the required OAuth Headers 
and stores the OAuth Header object in a file. The OAuth header object will be useful to the REST Client.


Using a rest API to get data from an OBP Server
-----------------------------------------------
The example shows getting the list of 'banks' from using the REST API.
The OAuth header is also passed along, useful to access protected resources.


Installation
------------
The installation is simple. Its just about installing the dependencies right.

.. code-block:: bash

    $ git clone git@github.com/pramttl/obp-python-client.git
    $ cd obp-python-client
    $ sudo pip install -r requirements.txt


Settings
--------
All the configuration parameters for OAuth 1.0 authentication (get-oauth-headers.py)
and access to REST API (rest-client.py) are defined in the settings file: "settings.py"
Most of the settings have been done appropriately for Open Bank Project Sandbox.
The Consumer Key and Secret needs to be set as per what you have received after
registering your applicatin on any one of the following:

> demo.openbankproject.com
> demo.openbankproject.com/sandbox

To switch from <sandbox mode> to <real mode>; in the settings.py file, 
just omit the '/sandbox' string, for all the settings variables where you see it.


Usage
-----

(1)
One time usage to get OAuth Token, and generate OAuth Headers.
(The generated Token, Headers are pickled into a text file)

.. code-block:: bash

    $ python get_oauth_headers.py

(2)
Accessing the resources provided by the OBP REST API.
The rest-client assumes that the OAuth headers are in place in the OAUTH_HEADER_OBJECT file.
(Generated once using the previous step)
Pass the absolute path of the resource as a command line argument.

.. code-block:: bash

    $ python rest-client.py <ABSOLUTE_RESOURCE_PATH>

Example:

.. code-block:: bash

    $ python rest-client.py /banks/postbank


