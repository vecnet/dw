# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

from django.views.generic import ListView
from collections import OrderedDict
from django.db.models import get_app, get_models
import inspect


class LookUpResults(ListView):
    """This view is used to render the lookup tables. It checks all
    models in the datawarehouse app for a field called lookup. If
    that field is found, then the model is queried and added to the
    results.
    """
    results = {}
    template_name = 'datawarehouse/luresults.html'  # template to render to

    def get_context_data(self, **kwargs):
        """This method generates context data that is returned to the template.
        """
        context = super(LookUpResults, self).get_context_data(**kwargs)  # call the super
        context['results'] = self.results  # add results to the context
        return context

    def get_queryset(self):
        """This method is responsible for getting the querysets and appending them
        to the results list.
        """
        app = get_app('datawarehouse')
        for model in get_models(app):  # loop over datawarehouse tables
            for f in inspect.getmembers(model):
                if f[0] == 'lookup' and f[1] == True:
                    self.results[model._meta.object_name] = [f.name for f in model._meta._fields()]

    def get_ordered_list(self, elements):
        """This method creates a list of ordered dictionaries using elements.
        """
        ordered = list()
        for obj in elements:
            od = OrderedDict((field.name, field.value_to_string(obj)) for field in obj._meta.fields)
            ordered.append(od)
        return ordered
