#!/usr/bin/env python
import os
import zipfile
from zipfile import ZipFile
import pysftp
import pysftp as sftp
import paramiko
from paramiko import SSHClient
import glob
import re
import getpass


# Create a zip backup of the current working directoy
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    print("Creating a ZIP backup file of the current working directory...\n")
    zipf = zipfile.ZipFile('backup.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(os.getcwd(), zipf)
    zipf.close()
    print("The below files have been archived in the zip file:\n")
    zipf.printdir()


# Connect to the SFTP server and upload the backup
sftp_passord = getpass.getpass("Please enter the SFTP server password to continue:\n")
hostname="34.247.156.147"
username="sftp"
password= sftp_passord
localFilePath = './backup.zip'
remoteFilePath = '/ubuntu/backup.zip'

print("Connecting to the SFTP server....\n")
with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
    print ("Connection succesfully stablished ...\n")

    # Switch to a remote directory
    sftp.cwd('/ubuntu/')

    # Obtain structure of the remote directory '/ubuntu/'
    directory_structure = sftp.listdir_attr()

    # Print data
    print("Below are the current contents of the remote SFTP server home directory:\n")
    for attr in directory_structure:
        print (attr.filename, attr)
        sftp.put(localFilePath, remoteFilePath)
print("The above backup file has been upload succesfuly...\n")
print("---------------------------------------------------\n")


user_confirmation = input("Are you sure you want to keep the last 3 files only:\n Please enter yes/no:")

if user_confirmation == "yes":
        print("The program will delete the zip archives and keep only the latest 3 files...\n")
        zipfiles = glob.glob("*.zip")
        zipfiles.sort()
        for ifl, fl in enumerate(zipfiles[:-3]):
            if zipfiles[ifl+1].startswith(fl[:1]):
                os.unlink(fl)

elif user_confirmation == "no":
        print("None of the archives will be deleted...\n")

else:
        print("Please select yes or no.")


'''
# Keep the latest 3 zip files only
print("Are you sure you want to keep the latest 3 zip archives only:")
zipfiles = glob.glob("*.zip")
zipfiles.sort()

for ifl, fl in enumerate(zipfiles[:-3]):
    if zipfiles[ifl+1].startswith(fl[:1]):    #Check if next file is same day
        os.unlink(fl)   
'''
