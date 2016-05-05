#!/bin/bash
docker run -i --net=host -v /home/mpas/mpasdocker/app:/home/user/LANL/app mpasio ./launch.sh
