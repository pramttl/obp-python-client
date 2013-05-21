Open Bank Project OAuth & REST Client
====================================

This code provides a sample OAuth 1.0 Python client, used to connect to
the Open Bank Project API. Although examples are created specifically for
the Open Bank Project OAuth provider, but the code can be suitably tweaked for any OAuth 1.0 provider.

The other objective is to be able to access Open bank Data via a REST Client, that uses the OAuth protocol.
This part of the code has been added to the REST Client explained ahead.

OAuth_Authentication + API_Consumption

Thus the 2 aspects involved are:

[1] Getting the OAuth access token from the OBP OAuth Provider. (get-oauth-headers.py)
[2] Using the Rest API to get data from the Open Bank Project API, Demo Application Server. (rest-client.py)

All the initial settings are defined in the "settings.py" file.

Getting the Access Token via OBP OAuth Provider.
----------------------------------------------------------------------------
This has been illustrated in the get-oauth-headers.py
The code manages to get the access token, to construct the required OAuth Header
and stores the OAuth Header object in a file.
The OAuth header object will be useful to the REST Client.


Using the REST API to get data from an OBP Server
-----------------------------------------------
The rest-client.py file do GET API calls by adding the OAuth header required to access the protected resources.


Installation
------------
The installation is simple, its just about installing the dependencies.

.. code-block:: bash

    $ git clone git://github.com/pramttl/obp-python-client.git
    $ cd obp-python-client
    $ sudo pip install -r requirements.txt


Settings
--------
All the configuration parameters for OAuth 1.0 authentication (get-oauth-headers.py)
and the access to the REST API (rest-client.py) are defined in the settings file: "settings.py"
Most of the settings have been done according to the Open Bank Project Sandbox.
The Consumer Key and Secret needs to be set as per what we have received after
registering the application on any one of the following:

> https://demo.openbankproject.com/consumer-registration
> https://demo.openbankproject.com/sandbox/consumer-registration

To switch from <sandbox mode> to <real mode>; in the settings.py file,
just omit the '/sandbox' string, for all the settings variables where you see it.


Usage
-----

(1)
One time usage to get the OAuth access token, and generate OAuth Headers.
(The generated token, headers are pickled into a text file)

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
