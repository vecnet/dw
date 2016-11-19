# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

# import statements
from collections import OrderedDict

from django.views.generic import TemplateView

from datawarehouse.cubes_config import dwmodel


class CubeView(TemplateView):
    """Used to render the index page of the datawarehouse browser.

    This adds all available cube names to the context dictionary
    """
    #: Template used to render the datawarehouse browser index page
    template_name = 'datawarehouse/cube.html'
    test = None

    def get_context_data(self, **kwargs):
        """Extension of the get_context_data method of the Templateview.

        Used to add on the cube names to the context dictionary
        """
        context = super(CubeView, self).get_context_data(**kwargs)
        context['nav_button'] = 0

        if self.test:
            context['test'] = True
        else:
            context['test'] = False
        cube_dict = OrderedDict()                                       # create an empty dictionary to hold the cube names
        for cube in dwmodel.cubes:
            print str(cube)
            cube_dict[str(cube)] = str(dwmodel.cube(cube).label)          # add the cubes to the dictionary
        context['cube_dict'] = OrderedDict(sorted(cube_dict.items(), key=lambda x: x[1], reverse=False))  # add the cube list to the context
        return context                                                  # return the context


