# MPAS

Instructions for running diverge after Randall's instructions at  *Launch a starcluster named <cluster>*

```bash
$ starcluster start -c <cluster> <cluster>
$ starcluster sshmaster <cluster>
```

Now you are on the cluster on AWS. Next is to clone the mpasdocker git repository
It is very important that you have to clone the mapsdocker git repository to the local directory where the shared data volume is mounted.
```bash
$ cd /home/mpas
$ git clone https://github.com/randalburns/mpasdocker.git
$ cd MPAS
```

Edit `hostfile` to represent the number of nodes on your `<cluster>`. In this case, we use a two-nodes cluster
Edit `machinefile` to represent the number of nodes *and* processors on your `<cluster>`

This builds your docker, which is one process per node.
```bash
$ mpirun -hostfile hostfile --mca btl_tcp_if_include eth0 ./mpibuild_mpas.sh --verbose --output-filename=mpibuild
```

This runs your simulation in docker, which is *n* processes per node.
```bash
$ mpirun -hostfile hostfile --mca btl_tcp_if_include eth0 ./mpirun_mpas.sh --verbose --output-filename=mpirun
```


<h3> Description of Files </h3>
  * Dockerfile -- build of MPAS and I/O libraries into a Docker container
  * mpibuild_mpas.sh -- script that builds the docker container on each node
  * mpirun_mpas.sh -- script to launch H3D with docker containers on each node 
  * runmpas.sh -- script that runs H3D inside a docker container on the master node.  DO NOT call this directly.  It is called by mpirun_mpas.sh
 
