# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
admin.autodiscover()
from django.contrib.auth.views import login, logout
from lib.views.error_views import view_server_error, error_submit

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Included App URLs

    # url(r'^$', include('lib.urls')),
    url(r'^$', RedirectView.as_view(url='/datawarehouse/'), name="index"),
    # url(r'^expert_emod/', include('expert_emod.urls')), made obsolete by ts_emod
    url(r'^datawarehouse/', include('datawarehouse.urls')),
    url(r'^accounts/login/', login, {'template_name': 'admin/login.html'}, name="auth_login"),
    url(r'^accounts/logout/', logout, name="auth_logout"),

    # error page URLS
    url(r'^500$', view_server_error, name="error_template_500"),
    url(r'^403$', view_server_error, {'template_name': '403.html'}, name="error_template_403"),
    url(r'^404$', view_server_error, {'template_name': '404.html'}, name="error_template_404"),
    url(r'^error_submit$', error_submit, name="submit_server_error"),
]

try:
    from .urls_local import urlpatterns_local
    urlpatterns += urlpatterns_local
except ImportError:
    urlpatterns_local = None

handler500 = 'lib.views.error_views.view_server_error'
