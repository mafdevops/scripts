#!/bin/bash
sudo apt update -y

# Instal OpenSSH
sudo apt install openssh-server

# Enable and start SSH
sudo systemctl enable ssh.service
sudo systemctl start ssh.service


sudo nano /etc/ssh/sshd_config
sudo systemctl restart ssh.service


sudo groupadd sftp_users

sudo usermod -aG sftp_users backup
passwd backup
