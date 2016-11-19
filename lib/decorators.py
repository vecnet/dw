# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def group_required(group, login_url=None, raise_exception=True):
    """
    Decorator for views that checks whether a user is a member of a group, redirecting to the log-in page if neccesary.
    If the raise_exception parameter is not given the PermissionDenied exception is raised.
    """
    def is_user_in_group(user, group):
        return user.groups.filter(name=group).exists()

    def check_group(user):
        # If user is not logged in, redirect them to login form
        if user.is_anonymous():
            return False
        # First check if the user is in a group
        if is_user_in_group(user, group):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_group, login_url=login_url)