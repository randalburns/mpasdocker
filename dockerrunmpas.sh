#!/bin/bash
cd /home/mpas/LANL/app/mpas_240km
mpiexec -machinefile /mnt/mpasrun/machinefile /mnt/mpasrun/LANL/app/mpas_240km/ocean_forward_model
#LD_LIBRARY_PATH=/usr/local/paraview.bin/lib mpiexec -machinefile /mnt/vpicrun/machinefile /mnt/vpicrun/vpic.bin/8preconnection.Linux
