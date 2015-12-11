########################################################################################################################
# VECNet CI - Prototype
# Date: 4/5/2013
# Institution: University of Notre Dame
# Primary Authors:
########################################################################################################################
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from lib.views.RevisionView import RevisionView

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Included App URLs

    # url(r'^$', include('lib.urls')),
    url(r'^$', RedirectView.as_view(url='/datawarehouse/'), name="index"),
    #url(r'^expert_emod/', include('expert_emod.urls')), made obsolete by ts_emod
    url(r'^datawarehouse/', include('datawarehouse.urls')),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'},
        name="auth_login"),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name="auth_logout"),
    #url(r'^login/', RedirectView.as_view(url=settings.LOGIN_URL), name="auth_login"),
    url(r'^revision$', RevisionView.as_view()),

    # error page URLS
    url(r'^500$', 'lib.views.error_views.view_server_error', name="error_template_500"),
    url(r'^403$', 'lib.views.error_views.view_server_error', {'template_name': '403.html'}, name="error_template_403"),
    url(r'^404$', 'lib.views.error_views.view_server_error', {'template_name': '404.html'}, name="error_template_404"),
    url(r'^error_submit$', 'lib.views.error_views.error_submit', name="submit_server_error"),
)

try:
    from .urls_local import urlpatterns_local
    urlpatterns += urlpatterns_local
except ImportError:
    pass

handler500 = 'lib.views.error_views.view_server_error'