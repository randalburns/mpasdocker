#!/bin/bash
docker run -i --net=host -v /vmshare:/mnt/mpasrun mpas /home/mpas/launch.sh
