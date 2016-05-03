#/bin/bash

cd /mnt/h3d/1.0/catalyst-build

WORKDIR=/mnt/h3d/1.0/catalyst-build/../src
PARAVIEW_BUILD_DIR=/usr/local/paraview.bin

export DATA_DIRECTORY=$WORKDIR/data
export RESTART_DIRECTORY=$WORKDIR/restart_files
export INPUT_DIRECTORY=$WORKDIR/../inputs
export SOURCE_DIRECTORY=$WORKDIR

mkdir -p $DATA_DIRECTORY
mkdir -p $RESTART_DIRECTORY

cp $INPUT_DIRECTORY/finput.small.dat $DATA_DIRECTORY/finput.dat
#cp $INPUT_DIRECTORY/finput.ssmall.dat $DATA_DIRECTORY/finput.dat

echo "CLEANUP_STATUS=FALSE" > $DATA_DIRECTORY/.cleanup_status

export MPI_TYPE_MAX=65536
export MPI_REQUEST_MAX=65536

cd /mnt/h3d/1.0/catalyst-build
rm -f *.png

echo "About to sleep"
sleep 10
echo "Slept"

LD_LIBRARY_PATH=$PARAVIEW_BUILD_DIR/lib mpiexec -machinefile /home/h3d/machinefile $WORKDIR/3dh > 3dhout.log 2>&1
#LD_LIBRARY_PATH=$PARAVIEW_BUILD_DIR/lib mpiexec -np 16 $WORKDIR/3dh > 3dhout.log 2>&1
#LD_LIBRARY_PATH=$PARAVIEW_BUILD_DIR/lib mpiexec -np 4 $WORKDIR/3dh > 3dhout.log 2>&1

