# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

import csv

from django.core.management.base import BaseCommand

from datawarehouse.models import LutInterventionIrsCoveragesAdmin1


class Command(BaseCommand):
    """
    This class defines the ETL command. The ETL command is used
    to ingest data given an input file and a mapping file. It is
    important to note that location is hardcoded due to the complicated
    nature of gis data. The rest of the class is dynamic and could be
    easily reused in other projects.
    """

    def handle(self, *args, **options):
        """This method is responsible for 'handling' the inputs.

        This method is the heart of the management command.
        It uses the given inputs, along with other methods, to ingest
        data.

        :param *args: Argument list.
        :param **options: Command line options list.
        """
        if len(args) == 0:
            print "Please specify filename"
            exit(0)
        filename = args[0]
        with open(filename, 'rb') as csvfile:
            irsdata = csv.reader(csvfile, delimiter=",")
            for row in irsdata:
                print row[1], row[0]
                # print ".%s." % float(row[4])
                irs = LutInterventionIrsCoveragesAdmin1()
                irs.gaul_code = int(row[0])
                irs.country = row[2]
                irs.province_name = row[1]
                try:
                    irs.percent_of_the_population_protected_by_irs = float(row[3])
                except ValueError:
                    irs.percent_of_the_population_protected_by_irs = None

                try:
                    irs.year = int(row[4])
                except ValueError:
                    print "ValueError: Year"
                    continue
                try:
                    irs.source = row[5]
                except ValueError:
                    print "ValueError: source"
                    continue
                irs.save()
        print options
        pass
