gapps-csv-pwd-sync
==================

A python utility to sync up a csv of username's and passwords to Google Apps

### Dependencies ###
* Python 2
* Google Data Libraries ( pip install gdata )

### Setup Instructions for Mac ###
1. Install a newer version of python:

        brew install python
      
2. Restart your terminal to load up the new version of python:

        relaunch terminal

3. Use pip to install the required Google Data Libraries 

        pip install gdata

### Usage Instructions ###
1. Create your CSV file in the format of "username,password". You can do this in excel using a column for username and the next
for password. Save this file in the same folder as this script.
2. Navigate to the folder this script is located in.
3. Execute the following, replacing the brackets with the corresponding values:
 
        ./sync_pwd.py [name of your csv file]

4. Bask in the glory of your success
