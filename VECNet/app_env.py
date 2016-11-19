# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

DEVELOPMENT = "dev"
QA = "qa"
PRODUCTION = "production"
ALL_KNOWN = (DEVELOPMENT, QA, PRODUCTION)

_app_env = None


def set(app_env):
    """
    Set the application environment.

    :param str app_env: One of the string constants defined above.
    :returns bool: True if the application environment is valid; False if it's invalid.
    """
    if app_env in ALL_KNOWN:
        global _app_env
        _app_env = app_env
        return True
    else:
        return False


def is_production():
    """
    Is the application running in a production environment?
    """
    return _app_env == PRODUCTION


def is_qa():
    """
    Is the application running in a QA environment?
    """
    return _app_env == QA


def is_development():
    """
    Is the application running in a development environment?
    """
    return _app_env == DEVELOPMENT
