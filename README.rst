Openbank Project Python OAuth Client
====================================

This code provides a sample OAuth1 Pythob client, used to connect to 
the Openbank Project API. Although examples are created specifically for 
the Openbankproject, but the code can be used for any OAuth1 provider.
The other objective is to be able to access Openbank Data via this client itself.

OAuth_Authentication + API_Consumption


There are 2 aspects involved.
(1) Getting Access Token via OBP OAuth Provider.
(2) Using a rest API to get data from an OBP Server

Getting Access Token via OBP OAuth Provider. (OAuth 3-Legged Authentication)
----------------------------------------------------------------------------
This has been inllustrated in the client.py code. 

Note: The code currently only demonstrates the OAuth 3-Legged Authentication, 
that is useful only for the first time,until you get the oauth_token.



Using a rest API to get data from an OBP Server
-----------------------------------------------
#TODO


Installation
------------
The installation is simple. Its just about installing the dependencies right.



.. code-block:: bash

    $git clone git@github.com/pramttl/obp-python-client.git
    $ sudo pip install -r requirements.txt


Usage
-----

One time usage to get OAuth Token.

.. code-block:: bash

    $ python client.py


