#!/bin/bash

sudo apt update

# installing python
#sudo apt -y install python3.8 python3.8-venv &&
#python3 -m venv env &&
source ./env/bin/activate &&
pip3 install -r requirements.txt &&
deactivate

# installing geckodriver for selenium
#mkdir -p ~/geckodriver && cd ~/geckodriver
#sudo apt install wget &&
#wget -O geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz &&
#tar xzvf geckodriver.tar.gz &&
#sudo chmod +x geckodriver &&
#zzzsudo mv geckodriver /usr/local/bin/