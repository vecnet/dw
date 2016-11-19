# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/
from django import forms


class dlform(forms.Form):
    # TODO Add class docstring
    file_name = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.HiddenInput())
