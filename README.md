# MPAS

Instructions for running diverge after Randall's instructions at  *Launch a starcluster named h3d*

```bash
$ starcluster start -c h3d <cluster>
$ starcluster sshmaster <cluster>
```

Now you are on the cluster on AWS.

```bash
$ mkdir /home/mpas
$ cd /home/mpas
$ git clone https://github.com/guanxyz/MPAS
$ cd MPAS
```

Edit `hostfile` to represent the number of nodes on your `<cluster>`
Edit `machinefile` to represent the number of nodes *and* processors on your `<cluster>`

This builds your docker, which is one process per node.
```bash
$ mpirun -hostfile hostfile --mca btl_tcp_if_include eth0 ./mpibuild_mpas.sh --verbose --output-filename=mpibuild
```

This runs your simulation in docker, which is *n* processes per node.
```bash
$ mpirun -hostfile hostfile --mca btl_tcp_if_include eth0 ./runmpas.sh --verbose --output-filename=mpirun
```
