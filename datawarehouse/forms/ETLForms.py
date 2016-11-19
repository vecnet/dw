# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

"""
This model defines the forms used in the ETL views.

Each form in this file is used in either the mapping or ingest steps of the ETL process.
"""

# import statements
import cStringIO
import requests
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile as IFile
from django.db.models.loading import get_app, get_models

from datawarehouse.forms.forms import dlform
from datawarehouse.views.ETLView import ETLWizard

URLHELP = "Instead of providing a local file, you may provide a URL. If you provide both, the local file will be used."


class UploadForm(forms.Form):
    """
    This class defines the initial form in the mapping wizard. It is
    used to upload an input file to the server for processing.
    """

    inputFile = forms.FileField(required=False)
    url = forms.URLField(help_text=URLHELP, required=False)

    def clean(self):
        """
        This method over-rides the default clean method. It adds a check
        that either an input file or a url was given. If a url was given
        but an input file wasn't, it attempts to get a file from the url.
        If it cannot get a valid file from the url, it raises a validation
        error.
        """
        cleaned_data = self.cleaned_data
        inputFile = cleaned_data.get("inputFile")
        url = cleaned_data.get("url")
        # must have either a valid url or a valid file
        if not inputFile and not url:
            raise forms.ValidationError("You must provide a valid input file or a valid url.")
        # if we have a url but no file, try to get a file from url
        elif not inputFile and url:
            try:
                r = requests.get(url)
            except Exception as e:
                raise forms.ValidationError(e)
            myfile = cStringIO.StringIO(r.content)
            myifile = IFile(myfile, 'upload-inputFile', 'tempfile', 'text/csv', len(r.content), None)
            self.files['upload-inputFile'] = myifile
            self.data['upload-url'] = ''  # this line avoids infinite recursion, because full_clean calls clean
            self.full_clean()

        # return the cleaned data.
        return cleaned_data


class MappingForm(forms.Form):
    """
    This class defines the form for the mapping page. In this phase,
    a mapping object is defined by the user. A hidden input field is
    used to hold the created mapping object.
    """

    mapping = forms.CharField(widget=forms.HiddenInput())


class TableForm(forms.Form):
    """
    This class creates a form to select a database table. The selected table,
    in conjunction with the input file, is used to create a mapping object in
    the next step.
    """

    # get the app, then the models in that app, then
    # corresponding database tables for those models
    app = get_app('datawarehouse')
    tableResults = [model._meta.db_table for model in get_models(app)]
    tableChoices = [(t, t) for t in tableResults]
    tables = forms.ChoiceField(widget=forms.Select(), choices=tableChoices)


#: This variable is used by the ETL wizard to determine the steps and their order.
steps = (
    ('upload', UploadForm),
    ('selectTable', TableForm),
    ('createMap', MappingForm),
    ('downloadMapping', dlform)
)

"""This variable is used in the urls file to correctly identify the form wizard."""
upload_wizard_view = ETLWizard.as_view(steps, url_name='datawarehouse_etl', done_step_name='complete')


class IngestionForm(forms.Form):
    """
    This class creates a form for ingesting data.  It contains a field for
    the input data and a field for the mapping object (which is responsible
    for determining how input columns relate to database columns).
    """

    inputFile = forms.FileField(required=False)
    inputURL = forms.URLField(help_text=URLHELP, required=False)
    mappingFile = forms.FileField(required=False)
    mappingURL = forms.URLField(help_text=URLHELP, required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        inputFile = cleaned_data.get("inputFile")
        inputURL = cleaned_data.get("inputURL")
        mappingFile = cleaned_data.get("mappingFile")
        mappingURL = cleaned_data.get("mappingURL")

        # must have either a valid url or a valid file
        if not inputFile and not inputURL:
            raise forms.ValidationError("You must provide a valid input file or a valid input url.")
        # if we have a url but no file, try to get a file from url
        elif not inputFile and inputURL:
            try:
                r = requests.get(inputURL)
            except Exception as e:
                raise forms.ValidationError(e)
            myfile = cStringIO.StringIO(r.content)
            myifile = IFile(myfile, 'inputFile', 'tempfile', 'text/csv', len(r.content), None)
            self.files['inputFile'] = myifile
            self.data['inputURL'] = ''  # this line avoids infinite recursion, because full_clean calls clean
            self.full_clean()

        # must have either a valid url or a valid file
        if not mappingFile and not mappingURL:
            raise forms.ValidationError("You must provide a valid mapping file or a valid mapping url.")
        # if we have a url but no file, try to get a file from url
        elif not mappingFile and mappingURL:
            try:
                r = requests.get(mappingURL)
            except Exception as e:
                raise forms.ValidationError(e)
            mymapfile = cStringIO.StringIO(r.content)
            mymapifile = IFile(mymapfile, 'mappingFile', 'tempmapfile', 'text/csv', len(r.content), None)
            self.files['mappingFile'] = mymapifile
            self.data['mappingURL'] = ''  # this line avoids infinite recursion, because full_clean calls clean
            self.full_clean()

        # return the cleaned data.
        return cleaned_data
