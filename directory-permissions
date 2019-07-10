#!/bin/bash

# Create a directory called: “test-directory” and a new file inside it called: “test.txt”:
mkdir test-directory && touch test-directory/test.txt

# change its permissions t oread only
chmod a-wx test- directory

# to check the new permission 
ls-alh

# add the execute permission
chmod a+x test-directory

# Check execute permission capabilities
ll
cd test-directory
cat test.txt

# try to rename/remove the file (will not work in execute permission)
mv test.txt test-2.txt
rm -r test.txt
