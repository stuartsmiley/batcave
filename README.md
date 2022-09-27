# Opening the Garage Door with a raspberry pi

```shell
$ pip install virtualenv
$ virtualenv venv
$ source ./venv/bin/activate
pip install Flask

```

```shell
$ sudo apt-get update
$ sudo apt-get install apache2 apache2-utils libexpat1 ssl-cert python
$ sudo apt-get install libapache2-mod-wsgi
$ sudo systemctl restart apache2
```


```shell
<Directory /var/www/>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
</Directory>
```

on the pi
```shell
$ sudo pip3 install flask uwsgi   

$ cd /var/www
$ sudo mkdir batcave
```
run deploy script

back on pi
```
$ sudo systemctl daemon-reload
$ sudo systemctl start batcave.service
$ sudo systemctl status batcave.service
$ sudo systemctl enable batcave.service

```