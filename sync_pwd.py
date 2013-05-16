#! /usr/bin/env python
import sys
import csv
import gdata.apps.client
import getpass

if len(sys.argv) != 2:
  print 'Please specific exactly one input CSV file in the format of username, password'
  exit()

print "\n Please login with your Google Apps Credentials (note you must be an admin)"
domain = raw_input("Domain: ")
admin_user = raw_input("Username: ")
admin_pass = getpass.getpass()

client = gdata.apps.client.AppsClient(domain=domain)
client.ssl = True
login_ok = client.ClientLogin(email=admin_user+'@%s' % domain, password=admin_pass, source='apps')
if not login_ok:
  print "invalid login"
  exit();


print 'Reading file "%s"\n' % sys.argv[1]
r = csv.reader(open(sys.argv[1], 'rb'))


header = raw_input("Does you csv file have a header row (a list of column names)? [y/n]")

if header == "yes" or header == "y":
  header = True
  print '\n Got it, your data HAS a header row.'
  r.next()


sanity_line=r.next()
print 'Please verity the data below is correct. This should be the first line of data in csv file:'
print 'Username: %s' % sanity_line[0]
print 'Password: %s' % sanity_line[1]
yn = raw_input("Is this data correct? [y/n]")


if yn != "yes" and yn != "y":
  print 'Please make sure your data is in the format username, password and your csv file does not have a header row'
  exit()

data = {}
with open(sys.argv[1], 'rb') as csvfile:
  pr = csv.reader(csvfile)
  if header == True:
     pr.next()
  for row in pr:
    #Username is row[0]
    #Password is row[1]
    data[row[0]] = row[1]

#data now contains all of our usernames and passwords
total_count = len(data)
error_count = 0
succeed_count = 0

#lets to check they all have google accounts
for username, password in data.iteritems():
  try:
    guser = client.RetrieveUser(username)
  except gdata.client.RequestError:
    guser = None

  if type(guser) is not gdata.apps.data.UserEntry:
    error_count += 1
    print 'ERROR: %s does not have a google apps account' % username

  guser.login.password = password
  update_ok = client.UpdateUser(username, guser)
  if not update_ok:
    print 'ERROR: Password change failed for %s' % username
    error_count += 1

  succeed_count += 1
  print 'SUCCESS: Password changed for %s' % username


print 'DONE: Processed %d records. %d succeeded. %d failed.' %(total_count, succeed_count, error_count)
