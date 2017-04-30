# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Used to render the index page of the datawarehouse browser.
    """
    #: Template used to render the datawarehouse browser index page
    template_name = 'datawarehouse/index.html'

    def get_context_data(self, **kwargs):
        """Extension of the get_context_data method of the Templateview.

        Used to add on the cube names and lookup table names
        to the context dictionary
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['nav_button'] = 0

        return context  
