#Overview

This is a preserved version of VecNet-CI Datawarehouse browser based on Django 1.5

#System requirements

This Django project has been tested on Windows 8 x64 and CentOS 7

#Quick Start Guide
1. Create database structures
    `./manage.py syncdb`

2. Load data
    `./manage.py loaddata dw.json`

3. Create an admin user
   `./manage.py createsuperuser`

#Database

This project requires Postgis extension to PostgreSQL database.

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

#Notes

1. ETL interface may be broken