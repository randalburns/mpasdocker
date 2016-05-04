#!/bin/bash

# if you are the master node run the code
if [ $HOSTNAME == 'master' ]; then

echo "Starting h3d on master"

# Move build files to nfs shared mount
chown -R user:user /home/user/LANL/app

# run the code as a user
su user -c /home/user/LANL/runmpas.sh 

# All slave nodes launch the ssh server
else

echo "Starting sshd"
mkdir /var/run/sshd
/usr/sbin/sshd -D

fi
