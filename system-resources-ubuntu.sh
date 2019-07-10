#!/bin/bash
sudo apt update

# Checking free system memory
vmstat -s

# Checking free disk space
df -H

# Checking CPU usage
sudo apt install -y sysstat
iostat

# Count number of lines in a file: create a new file, add contents to it from a URL, and count the total number of lines: 
touch numberoflines.txt
wget "https://ubuntu.com/about" -O numberoflines.txt
wc –l numberoflines.txt


# Open TCP port: Let's install Apache web server, stop the service, check the opened ports, then open the port and check it
    # Install Apache
sudo apt install -y apache2
sudo ufw app list
sudo ufw allow 'Apache'

    # Check its port, it shoild be listening to 80
netstat -tulpn
    # Stop Apache service
sudo systemctl stop apache2
    # Check its portagain, it shouldn't be listed
netstat -tulpn
    # Do the same to re-open the port by starting the service
sudo systemctl start apache2 && netstat -tulpn
