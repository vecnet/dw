# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

from django.views.generic import TemplateView


def IsIngestor(user):
    """Check if a user is an ingestor.

    This function is used to check if a User belongs to the 'ingestor'
    group. This is used to restrict access to the IngestionView, so that only
    users designated as ingestors can ingest data.

    :param user: The user to identify as an Ingestor or not.
    :return: A Boolean indicating whether the given user was in the ingestor group.
    """

    if user:
        return user.groups.filter(name='ingestor').exists()
    return False


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

        # if the user has ingestion rights, push a boolean into the context, which is used by the template to display
        # links to the ingestion pages
        if IsIngestor(self.request.user):
            context['isIngestor'] = True

        return context  
