from randalburns/pvcat:mpich
MAINTAINER qguan "qguan@lanl.gov"

# The proxy is for Darwin and other machines within LANL.
ENV http_proxy 'http://proxyout.lanl.gov:8080'
ENV https_proxy 'http://proxyout.lanl.gov:8080'
ENV no_proxy 'localhost,127.0.0.1'
RUN echo 'Acquire::http::Proxy "http://proxyout.lanl.gov:8080";' >> /etc/apt/apt.conf.d/docker-clean


RUN apt-get -y update
RUN apt-get -y install\
  build-essential\
  ctags\
  curl\
  vim\
  bison\	
  flex\	
  subversion\
  python-setuptools\	
  ruby\		
  wget

##################################################
# Install brew
##################################################
RUN git clone https://github.com/Linuxbrew/linuxbrew.git ~/.linuxbrew
RUN echo "export PATH="$HOME/.linuxbrew/bin:$PATH"" >> ~/.bashrc
RUN echo "export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH""  >> ~/.bashrc
RUN echo "export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"">> ~/.bashrc

##################################################
# Add active user "mpas"  (mpas:mpas)
##################################################
RUN groupadd -r mpas && useradd -r -m -g mpas mpas

##################################################
# TO-DO :Configure the No-Password SSH in docker
##################################################
#COPY  ~/.ssh/id_rsa.pub  /home/user/.ssh/
#RUN cat /home/user/.ssh/id_rsa.pub >> /home/user/.ssh/authorized_keys
#RUN chown -R user:user /home/user/.ssh; chmod 0700 -R /home/user/.ssh
#RUN cat /root/.ssh/id_rsa.pub >> /home/user/.ssh/authorized_keys
# Asume that we are using the openmpi now!
# RUN sed -i 's/Port 22/Port 9222/' /etc/ssh/sshd_config
COPY id_rsa /home/mpas/.ssh/
COPY id_rsa.pub /home/mpas/.ssh/
COPY config /home/mpas/.ssh/
RUN chown -R mpas:mpas /home/mpas/.ssh; chmod 0700 /home/mpas/.ssh; chmod 0600 /home/mpas/.ssh/*
RUN sed -i 's/Port 22/Port 9222/' /etc/ssh/sshd_config

# add no password login
RUN cat /home/mpas/.ssh/id_rsa.pub >> /home/mpas/.ssh/authorized_keys

RUN chown -R mpas:mpas /home/mpas
##################################################
# Build the directories
##################################################
USER mpas
WORKDIR /home/mpas
RUN mkdir LANL LANL/libs LANL/MPAS LANL/temp
RUN mkdir LANL/libs/netcdf LANL/libs/pnetcdf LANL/libs/pio
RUN mkdir LANL/libs/pio/lib LANL/libs/pio/include
RUN chmod -R ug+rw /home/mpas/LANL

#################################################
# Setup environment
##################################################
# For the paths
##################
ENV MPAS_PATH /home/mpas/LANL
ENV MPAS_LIBS_PATH /home/mpas/LANL/libs
ENV IO_DEST $MPAS_LIBS_PATH/io
ENV NETCDF_C_SOURCE $MPAS_LIBS_PATH/netcdf-4.3.2
ENV NETCDF_F_SOURCE $MPAS_LIBS_PATH/netcdf-fortran-4.4.1
ENV PNETCDF_SOURCE $MPAS_LIBS_PATH/parallel-netcdf-1.5.0
ENV PIO_SOURCE $MPAS_LIBS_PATH/pio1_7_1/pio

ENV NETCDF_PATH $IO_DEST
ENV PNETCDF_PATH $IO_DEST

ENV F77 gfortran
ENV F90 gfortran
ENV CC gcc
ENV FC gfortran
ENV MPIFC mpif90
ENV MPIF77 mpif77
ENV MPIF90 mpif90
ENV MPICC mpicc

ENV CFLAGS -I$IO_DEST/include
ENV FFLAGS -I$IO_DEST/include
ENV LDFLAGS -L$IO_DEST/lib


#################################################
# Copy the libs
#################################################
COPY MPAS-io-libs.tar.gz $MPAS_PATH
WORKDIR $MPAS_PATH
RUN tar zxvf MPAS-io-libs.tar.gz


#################################################
# Build netcdf-c
#################################################
WORKDIR $MPAS_LIBS_PATH
RUN mkdir netcdf-c-build
WORKDIR $MPAS_LIBS_PATH/netcdf-c-build
RUN $NETCDF_C_SOURCE/configure --prefix=$IO_DEST --disable-shared --disable-netcdf-4 --disable-dap --disable-utilities || exit 1;
RUN make || exit 1;
RUN make install

#################################################
# Build netcdf-f
#################################################
WORKDIR $MPAS_LIBS_PATH
RUN mkdir netcdf-f-build
WORKDIR $MPAS_LIBS_PATH/netcdf-f-build
RUN $NETCDF_F_SOURCE/configure --prefix=$IO_DEST --disable-shared || exit 1;
RUN make || exit 1;
RUN make install

#################################################
# Build pnetcdf
#################################################
WORKDIR $MPAS_LIBS_PATH
RUN mkdir pnetcdf-build
WORKDIR $MPAS_LIBS_PATH/pnetcdf-build
RUN $PNETCDF_SOURCE/configure --prefix=$IO_DEST --disable-cxx || exit 1;
RUN make 
RUN make install

#################################################
# Build pio
#################################################
WORKDIR $PIO_SOURCE
RUN ./configure --prefix=$IO_DEST || exit 1;
RUN make clean || exit 1;
RUN make || exit 1;
RUN make install


#################################################
# clean
#################################################
WORKDIR $MPAS_LIBS_PATH
RUN rm -rf netcdf-c-build netcdf-f-build pnetcdf-build


# Install MPAS
RUN mkdir $MPAS_LIBS_PATH/MPAS
WORKDIR $MPAS_LIBS_PATH/MPAS
RUN git clone https://github.com/MPAS-Dev/MPAS-Release.git
#RUN wget https://github.com/MPAS-Dev/MPAS-Release/archive/v3.3.tar.gz
#RUN tar zxvf v3.3.tar.gz
WORKDIR $MPAS_LIBS_PATH/MPAS/MPAS-Release

# from make.sh by John Woodring
USER root
RUN ln -s `which python2` python
ENV PATH `pwd`:$PATH

ENV NETCDF $IO_DEST
ENV PNETCDF $IO_DEST
ENV PIO $IO_DEST

ENV CORE ocean
ENV MODE forward
ENV AUTOCLEAN true

# For fixing the bug by adding sync
RUN sed -i '/chmod/ c\		(chmod a+x get_cvmix.sh; sync; ./get_cvmix.sh)' src/core_ocean/Makefile

RUN make gfortran


#################################################
# Input Stack
#################################################
# You can use wget to get the input stack but we 
# cannot mount the data volume during the building
# time.
ADD launch.sh $MPAS_PATH
ADD launch_sshd.sh $MPAS_PATH
ADD dockerrunmpas.sh $MPAS_PATH
ADD machinefile $MPAS_PATH
#CMD chown user:user launch.sh && chown user:user runmpas.sh && chown user:user machinefile

WORKDIR $MPAS_PATH
USER root
# You can also use -v during docker run to mount
# the data volume 




