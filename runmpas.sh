#/bin/bash

# You MUST go to your app directory directly with ocean binary at the same level
cd /home/user/LANL/app/mpas_240km
mpiexec -machinefile /home/user/LANL/machinefile /home/user/LANL/app/mpas_240km/ocean_forward_model
