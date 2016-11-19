# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

from collections import OrderedDict
from django.http import HttpResponse
import simplejson


class JSONMixin(object):
    """This class was designed to be inherited and used to return JSON objects from an Ordered Dictionary
    """

    # Ordered Dictionary used to create serialized JSON object
    # return_rderedDict() #This will enforce the ordering that we recieve from the database

    def __init__(self):
        """
        Init function for the JSON Mixin class
        """
        self.return_list = OrderedDict()

        return

    def render_to_response(self, context):
        """Extends default render to response to return serialized JSON.
        """
        return self.get_json_response(self.convert_to_json())

    def get_json_response(self, content, **httpresponse_kwargs):
        """Returns JSON to calling object in the form of an http response.
        """
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)

    def convert_to_json(self):
        """Serialized the return_list into JSON
        """
        return simplejson.dumps(self.return_list)
