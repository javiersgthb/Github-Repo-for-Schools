#!/bin/bash

#This script creates multiple users based on an array of usernames.
#
# Username array
usernames=("atanaka" "alee" "rpatel")

#create the users by looping through the array
for username in "${usernames[@]}"
do
        sudo useradd -m -s /bin/bash "$username"
done

echo "Successfully created users"
sudo tail -n 3 /etc/passwd