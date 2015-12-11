# Copyright (C) 2015, University of Notre Dame
# All rights reserved

from fabric.api import local, sudo


def update():
    local('git pull')
    local('pip install -r requirements.txt')
    local('touch django.log')
    sudo('chown $USER:apache django.log')
    local('chmod g+w django.log')
    local('python manage.py syncdb')
    local('python manage.py collectstatic --noinput')
    local('touch wsgi.py')
