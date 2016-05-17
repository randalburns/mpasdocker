#!/bin/bash
echo `hostname`
docker build -f Dockerfilempasio -t mpasio /home/docker/mpasdocker
