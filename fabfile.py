# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

from fabric.api import local, sudo


def update():
    local('git pull')
    local('pip install -r requirements.txt')
    local('touch django.log')
    local('sudo chown $USER:apache django.log')
    local('chmod g+w django.log')
    local('python manage.py syncdb')
    local('python manage.py collectstatic --noinput')
    local('touch wsgi.py')
