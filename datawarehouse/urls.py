# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

from django.conf.urls import url, include   # keep include for now, until we separate these into 2 apps

from datawarehouse.views.CubeResultsView import CubeResultsView
from datawarehouse.views.CubeView import CubeView
from datawarehouse.views.IndexView import IndexView
from datawarehouse.views.LookupTablesView import LookupTablesView
from datawarehouse.views.SliceBrowser import SliceBrowser

urlpatterns = [
       url(r'^$', IndexView.as_view(), name='datawarehouse_index'),

       # Lookup tables - Alex
       url(r'^lookuptables/(?P<table_name>.+)/$', LookupTablesView.as_view(), name='datawarehouse_lookuptables'),
       url(r'^lookuptables/$', LookupTablesView.as_view(), name='datawarehouse_lookuptables'),

       # Datawarehouse browser - Larry
       url(r'SliceBrowser', SliceBrowser.as_view(), name='datawarehouse_sliceBrowser'),
       url(r'^cube$', CubeView.as_view(test=False), name='datawarehouse_cube'),
       url(r'^results/$', CubeResultsView.as_view(), name='datawarehouse_cube_results'),
]