FROM 	ubuntu:16.04
MAINTAINER warsang <theodore.riera@gmail.com>


#Default command on startup
CMD /bin/bash

#Change workdir
WORKDIR /home

#Setup packages
RUN apt-get update
RUN apt-get install -y --allow-unauthenticated git python2.7 python-pip python3 python3-pip libpcap-dev libpq-dev locales python3-tk wget unzip --fix-missing

RUN locale-gen en_US.UTF-8 fr_CA.UTF-8
ENV LANG en_US.UTF-8

#Get netgoblin
RUN git clone https://github.com/conix-security/netgoblin
WORKDIR /home/netgoblin/netzob
RUN git checkout develop
RUN pip3 install -r requirements.txt
RUN python3 setup.py install
#Move the Import file to install location. The setup.py seems broken, this is a temporary fix
RUN cp -r /home/netgoblin/netzob/src/netzob/Import/ /usr/local/lib/python3.5/dist-packages/Netzob-1.0.2-py3.5-linux-x86_64.egg/netzob/

#Get TAPIRE
WORKDIR /home
RUN git clone https://github.com/conix-security/TAPIRE
WORKDIR /home/TAPIRE
RUN git checkout develop
RUN pip3 install -r requirements.txt

#Get KAITAI struct
WORKDIR /home
RUN wget https://bintray.com/artifact/download/kaitai-io/universal/0.7/kaitai-struct-compiler-0.7.zip
RUN unzip kaitai-struct-compiler-0.7.zip
RUN rm kaitai-struct-compiler-0.7.zip

#Set workdir back to TAPIRE
WORKDIR /home/TAPIRE

