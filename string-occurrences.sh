#!/bin/bash
sudo apt update -y

# create a new file from the source of about AWS page 
curl "https://aws.amazon.com/about-aws/" > stringnumber.txt

# search for AWS string in the file
grep -o -i aws stringnumber.txt | wc -l

# Now, let's count the word: service, the output will include services as well
# for example, the command will grep "service" as a word  and amazon web "service"s as it's part of the line.
grep -o -i service stringnumber.txt | wc -l

# To count the whole word
grep -o '\<service\>' stringnumber.txt | wc -l
