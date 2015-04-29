#!/usr/bin/en python
#
import json
import subprocess
import ConfigParser

#from ipalib import api
#from ipalib import errors



configParser = ConfigParser.RawConfigParser()
configFilePath = r'ipa-access.conf'
configParser.read(configFilePath)

"""
Populate global variables
"""
admin_user = configParser.get('ipa-auth', 'admin_user')
admin_password = configParser.get('ipa-auth', 'admin_password')
ipa_realm = configParser.get('ipa-auth', 'ipa_realm')

if __name__ == "__main__":
	print admin_password
	print admin_user
	print ipa_realm