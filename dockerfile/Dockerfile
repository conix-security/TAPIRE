FROM 	ubuntu:16.04
MAINTAINER warsang <theodore.riera@gmail.com>


#Default command on startup
CMD /bin/bash

#Change workdir
WORKDIR /home

#Setup packages
RUN echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main" >> /etc/apt/sources.list.d/clang.list
RUN echo "deb-src http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main" >>  /etc/apt/sources.list.d/clang.list
RUN apt-get update
RUN apt-get install -y --allow-unauthenticated git python2.7 python-pip python3 python3-pip libpcap-dev libpq-dev locales python3-tk --fix-missing

RUN locale-gen en_US.UTF-8 fr_CA.UTF-8
ENV LANG en_US.UTF-8

#Get netgoblin
RUN git clone https://github.com/conix-security/netgoblin
WORKDIR /home/netgoblin/netzob
RUN git checkout develop
RUN pip3 install setuptools
RUN pip3 install minepy
RUN pip3 install -r requirements.txt
RUN python3 setup.py install

#Get TAPIRE
WORKDIR /home
RUN git clone https://github.com/conix-security/TAPIRE
RUN git checkout develop
WORKDIR /home/TAPIRE
RUN pip3 install -r requirements.txt


