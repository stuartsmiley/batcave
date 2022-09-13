#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "usage: deploy.sh <ip of your pi>"
    exit 1
fi

scp ../html/* pi@$1:
scp ../src/*.py pi@$1:
scp ../pi-plumbing/batcave.ini pi@$1:
scp ../pi-plumbing/batcave_proxy pi@$1:
scp ../pi-plumbing/batcave.service pi@$1:
ssh pi@$1  "sudo mv *.html /var/www/html && sudo mv *.png /var/www/html"
ssh pi@$1  "sudo mv *.py /var/www/batcave"
ssh pi@$1 "sudo mv batcave.ini /var/www/batcave"
ssh pi@$1 "sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default_bak_`date +"%d-%m-%Y"`"
ssh pi@$1 "sudo mv batcave_proxy /etc/nginx/sites-available && sudo ln -s /etc/nginx/sites-available/batcave_proxy /etc/nginx/sites-enabled/batcave_proxy"
ssh pi@$1 "sudo mv batcave.service /etc/systemd/system && sudo chown root:root /etc/systemd/system/batcave.service && sudo chmod 644 /etc/systemd/system/batcave.service"