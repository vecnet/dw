# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

import os
from . import app_env

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(PROJECT_PATH, os.pardir)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Used to construct absolute URLs for the site (e.g., for its REST APIs)
SITE_ROOT_URL = 'https://dw.vecnet.org/'

try:
    from .settings_local import APP_ENV
except ImportError:
    APP_ENV = os.environ.get('APP_ENV', app_env.DEVELOPMENT)  # Default to dev so developers don't need to set env var

if not app_env.set(APP_ENV):
    raise ValueError('Invalid value for APP_ENV: "%s"' % APP_ENV)

DEBUG = True

# LOG_FILE
try:
    from .settings_local import LOG_FILE
except ImportError:
    LOG_FILE = os.path.join(PROJECT_ROOT, 'django.log')


ADMINS = (
    ('Alexander Vyushkov', 'avyushko@nd.edu'),
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DEFAULT_DATABASE = {
    'ENGINE':  'django.contrib.gis.db.backends.postgis',
#    'ENGINE':  'django.contrib.gis.db.backends.postgresql',
    'NAME': "dw",
    'USER': "dw",
    'PASSWORD': "dw",
    'HOST': "127.0.0.1",
    'PORT': 5432,
    'TEST_NAME': os.environ.get('VECNET_TEST_DB', 'test_dw')
}

try:
    from .settings_local import DEFAULT_DATABASE as IMPORTED_DEFAULT_DATABASE
    DEFAULT_DATABASE.update(IMPORTED_DEFAULT_DATABASE)
except ImportError:
    pass

DATABASES = {
    'default': DEFAULT_DATABASE,
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Indiana/Indianapolis'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')t#af)a+(*+ers*%dukl495s&&&kkksjq0h+'

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )

# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.core.context_processors.static",
#     "django.core.context_processors.tz",
#     "django.contrib.messages.context_processors.messages",
#     'django.core.context_processors.request',
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'website', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'lib.context_processors.app_env',
                'lib.context_processors.app_dim_user',
            ],
        },
    },
]
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.RemoteUserBackend',
# )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'lib.middleware.CreateDimUserMiddleware'
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'VECNet.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'VECNet.wsgi.application'

# TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', '../lib', 'templates').replace('\\', '/'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    # Installed app for geodjango
    'django.contrib.gis',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'lib',
    'datawarehouse',
)

try:
    # Note that use can completely override list of INSTALLED_APPS by
    # re-defining INSTALLED_APPS variable in settings_local.py
    # INSTALLED_APPS_LOCAL will be ignored in this case
    from .settings_local import INSTALLED_APPS_LOCAL
    INSTALLED_APPS = INSTALLED_APPS + INSTALLED_APPS_LOCAL
except ImportError:
    INSTALLED_APPS_LOCAL = None
    pass

EMAIL_HOST = "smtp.nd.edu"
EMAIL_PORT = 25
EMAIL_USE_TLS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'prod_handler': {
            'level': 'INFO',
            'filters': [],
            'formatter': 'simple',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            # 'when': 'D',
            # 'interval': 1,
            # 'backupCount': 7
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'prod_logger': {
            'handlers': ['prod_handler'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/?next=/datawarehouse"

# django-debug-toolbar settings
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# settings for lib.middleware.LoginRequiredMiddleware
LOGIN_EXEMPT_URLS = ['ts_emod/', 'datawarehouse/', 'cifer/', 'om_validate/' '500', '404', '403']

# Use SERVER_MAINTENANCE_MESSAGE variable to set site-wide notification
# SERVER_MAINTENANCE_MESSAGE = "EMOD jobs submission system is being upgraded.<Br> Please do not not submit new EMOD jobs at this time."

DATABASE_BACKUP_DIR = MEDIA_ROOT

try:
    # Optional settings specific to the local system (for example, custom
    # settings on a developer's system).  The file "settings_local.py" is
    # excluded from version control.
    from .settings_local import *
except ImportError:
    pass
