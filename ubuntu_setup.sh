#!/bin/bash

if [ ! -f /home/vagrant/.setup_complete ] 
then
    echo 'deb http://archive.ubuntu.com/ubuntu precise multiverse' >> /etc/apt/sources.list;
    sudo apt-get update;
    sudo apt-get -y install htop wget curl multitail;
    sudo apt-get -y install python-pip python-virtualenv python-dev libpq-dev libzmq-dev;
    sudo apt-get -y install libjpeg8 zlib1g;
    #sudo apt-get -y install nginx-extras;

    #sudo pip install uwsgi ipython tornado;
    #sudo pip install pyzmq -b /tmp;

    sudo apt-get -y install git vim;
    sudo apt-get -y install bash-completion zip unzip;
    touch /home/vagrant/.setup_complete;
fi

