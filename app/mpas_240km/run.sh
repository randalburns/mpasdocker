#!/bin/bash

# export basedir=/home/user/LANL/MPAS
# export rundir=$basedir/mpas_240km

mpirun -np 4 ./ocean_forward_model
