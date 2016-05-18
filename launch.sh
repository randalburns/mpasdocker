#!/bin/bash

## make the run directory belong to vpic
cp -r /home/mpas/* /mnt/mpasrun/
#mkdir -p /mnt/vpicrun/vpic.bin
#mkdir -p /mnt/vpicrun/vpicrun1
#mkdir -p /mnt/vpicrun/vpicrun2
chown -R mpas:mpas /mnt/mpascrun/*
#
# run the vpic code  on master
su mpas -c /home/mpas/dockerrunmpas.sh
