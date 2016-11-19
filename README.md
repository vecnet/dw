#Overview

This is a preserved version of VecNet-CI Datawarehouse browser

The Data Warehouse Browser is a collection of two tools, Dimensional Data Browser and Lookup Tables Browser

**Dimensional Data**

Data Warehouse. The topics covered there are fairly diverse. From weather for many different locations, to how many bednets were covered in the last World Malaria 
Report Household Survey. You can search through this information by country, date, and aggregate across these fields to 
do some basic analysis.

**Lookup Tables**

is a place where you can look at information collected by experts on topics like bionomics.

#System requirements

This Django project has been tested on Windows 10 x64 and CentOS 7

#Quick Start Guide
1. Create database structures
    `./manage.py syncdb`

2. Load data. Database dump is in box.net (private) folder https://notredame.app.box.com/files/0/f/5725509665/1/f_46462663401
 and in CurateND - https://curate.nd.edu/concern/datasets/pg15bc40m5q
Make sure you have enough RAM to load the dump (4Gb is not enough, 16Gb worked).
    `./manage.py loaddata dw.json`

3. Create an admin user
   `./manage.py createsuperuser`

#Database

This project requires Postgis extension to PostgreSQL database.
Make sure custom SQL in datawarehouse/sql/dimdata.sql is loaded.

#Using Vagrant

1. Create Virtualbox VM `vagrant up`. It may take a while when starting VM for the first time

2. Login to VM using `vagrant ssh` command or your favorite ssh client. Login: vagrant, password vagrant

3. Switch to /vagrant directory `cd /vagrant`

4. Start django server `python manage.py runserver 0.0.0.0:8000`
Note you have to use 0.0.0.0 as server address, otherwise port forwarding may not work

You can edit files in your project directory, and changes will be visible to the virtual machine
(in /vagrant directory)

Credentials

*SSH* Login: vagrant, password vagrant

*PostgreSQL* Database: dw, Login: dw, Password: dw

*Note*: To utilize the PostgreSQL database, create a `settings_local.py` file containing the following:
```python
DATABASES = {
	'default': {
		'ENGINE': 'django.contrib.gis.db.backends.postgis',
		'NAME': 'dw',
		'USER': 'dw',
		'PASSWORD': 'dw',
		'HOST': '127.0.0.1',
		'PORT': '5432',
	}
}
```

# Production deployment checklist

1. Set DEBUG to False in settings_local.py

2. Generate new SECRET_KEY
 
3. Change ALLOWED_HOSTS and ADMINS accordingly

4. Set APP_ENV to 'production'

# Enable VecNet SSO

1. Install django-auth-pubtkt package

NOTE: on RedHat/CentOS install M2Crypto using command below first
`env SWIG_FEATURES="-cpperraswarn -includeall -I/usr/include/openssl" pip install M2Crypto`

`pip install django-auth-pubtkt`


2. Copy public key for validating pubtkt tickets to /etc/httpd/conf/sso/tkt_pubkey_dsa.pem

3. Enable DjangoAuthPubtkt middleware. Note if you choose to keep standard Django authentication backends, 
then django_auth_pubtkt.DjangoAuthPubtkt should after them.
```python
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_auth_pubtkt.DjangoAuthPubtkt',
    'django.contrib.messages.middleware.MessageMiddleware',
)
```

4. Set configuration options below
```python
LOGIN_URL = "/sso/"
LOGOUT_URL="https://www.vecnet.org/index.php/log-out"
TKT_AUTH_LOGIN_URL = "https://www.vecnet.org/index.php/sso-login"
TKT_AUTH_PUBLIC_KEY = '/etc/httpd/conf/sso/tkt_pubkey_dsa.pem'
```

5. Add the following lines to the urls.py file in the project for the site to redirect correctly:
```python
from django_auth_pubtkt.views import redirect_to_sso
url(r'^sso/', redirect_to_sso),
```

# Running project on Windows
Line below may be required in settings_local.py
```GEOS_LIBRARY_PATH = "c:\\Program Files\\GDAL\\geos_c.dll"```

Path to GDAL library should be in PATH env variable:
```PATH=%PATH%,C:\\Program Files\GDAL```

#Notes

1. ETL interface may be broken