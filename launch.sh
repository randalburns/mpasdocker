#!/bin/bash

# if you are the master node run the code
if [ $HOSTNAME == 'master' ]; then

echo "Starting h3d on master"

# Move build files to nfs shared mount
cp -r /home/mpas/* /mnt/mpas
chown -R user:user /mnt/mpas/* 

# run the code as h3d user
su user -c /home/mpas/runmpas.sh 

# All slave nodes launch the ssh server
else

echo "Starting sshd"
mkdir /var/run/sshd
/usr/sbin/sshd -D

fi
