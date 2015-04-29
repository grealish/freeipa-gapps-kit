# -*- coding: utf-8 -*-
# python
import json
import subprocess
import pprint


# Read in JSON file from Google Directors

my_data = json.loads(open("google-dirapi-monetas.net-userdump.json").read())

allusers = my_data.get('users', [])
#print json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': '))
for user in allusers:
	userid = user.get('id', {})
	primaryemail = user.get('primaryEmail', {})
	firstname = user.get('name', {}).get('givenName', {})
	lastname = user.get('familyName', {})
	displayname = user.get('name', {}).get('fullName', {})
	print 'userID:', userid, ' for ', displayname, ' with email: ', primaryemail
	
