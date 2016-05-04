#!/bin/bash
docker run -i --net=host -v /home/mpas/MPAS/app:/home/user/LANL/app mpasio ./launch.sh
