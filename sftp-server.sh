#!/bin/bash
sudo apt update -y

# Instal OpenSSH
sudo apt install openssh-server

# Enable and start SSH
sudo systemctl enable ssh.service
sudo systemctl start ssh.service

# Configure sftp and restart ssh service
sudo nano /etc/ssh/sshd_config
sudo systemctl restart ssh.service

# create new group for sftp called sftp_users
sudo groupadd sftp_users

# create new user called backup, add it to the group, and set his password
sudo usermod -aG sftp_users sftp
passwd sftp

# giev the grou pwrite permission to user home directory 
sudo chgrp -R sftp_users /home/ubuntu/
sudo chmod -R g+w /home/ubuntu/
