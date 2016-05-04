#!/bin/bash
docker run -i --net=host -v /home/mpas/mpasrun:/mnt/mpas mpasio ./launch.sh
