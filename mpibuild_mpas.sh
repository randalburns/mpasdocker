#!/bin/bash
echo `hostname`
docker build -f Dockerfilempasio -t mpasio /home/mpas/MPAS
