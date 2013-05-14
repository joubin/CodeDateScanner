#!/bin/bash
#Debian Setup

pwd=$(pwd)
if [ [ $EUID -nq 0 ] ]
then
	echo "Run this script with root"
	exit 1
fi

easy_install --version > /dev/null
if [ $? -ne 0 ]
then
	apt-get install python-setuptools -y 
fi

pip --version > /dev/null
if [ $? -ne 0 ]
then
	apt-get install python-pip -y
fi

sudo apt-get install python-dev -y 
sudo pip install fabric
sudo easy_install BeautifulSoup4
