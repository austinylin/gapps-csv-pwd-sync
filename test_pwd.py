#! /usr/bin/env python
import sys
import csv
import gdata.apps.client
import getpass

print "\n Please login with your Google Apps Credentials"
domain = raw_input("Domain: ")
admin_user = raw_input("Username: ")
admin_pass = getpass.getpass()

client = gdata.apps.client.AppsClient(domain=domain)
client.ssl = True
login_ok = client.ClientLogin(email=admin_user+'@%s' % domain, password=admin_pass, source='apps')
if not login_ok:
  print "invalid login"
  exit();

print 'SUCCSESS'
