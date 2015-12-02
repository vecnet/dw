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