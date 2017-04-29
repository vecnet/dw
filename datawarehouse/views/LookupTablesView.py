# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/
from collections import OrderedDict

from django.views.generic.base import TemplateView

from datawarehouse.models import LutSpecies, LutEntomologicalEndpoint, LutInterventionItnCoveragesAdmin1, \
    LutInterventionIrsCoveragesAdmin1, LutRepresentativeWorkflowParameters, LutVectorSpeciesParameter, \
    LutVectorSpeciesSensitivityParams

tables = OrderedDict([
    ("lut_species", LutSpecies, ),
    ("lut_ento_endpoints", LutEntomologicalEndpoint,),
    ("lut_itn", LutInterventionItnCoveragesAdmin1,),
    ("lut_irs", LutInterventionIrsCoveragesAdmin1,),
    ("lut_repr", LutRepresentativeWorkflowParameters,),
    ("lut_vector_species_params", LutVectorSpeciesParameter,),
    ("lut_vector_species_sensitivity_params", LutVectorSpeciesSensitivityParams,),
])

class LookupTablesView(TemplateView):
    template_name = "datawarehouse/lookup_tables.html"
    def get_context_data(self, **kwargs):
        table_name = kwargs.get("table_name", "lut_species")
        klass = tables[table_name]
        return {"klass": klass, "objects": klass.objects.all(), "tables": tables}
