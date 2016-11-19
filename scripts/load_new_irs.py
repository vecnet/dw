# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VECNet.settings")

from datawarehouse.models import DimLocation, DimDate, DimSource, FactWmrIrsOprtnlCvrg


def get_number(value):
    if value is None:
        return None
    value = value.replace(",", "").strip()
    if "-" in value or not value:
        return None
    try:
        return int(value)
    except ValueError as e:
        print e
        return None

if __name__ == '__main__':
    fp = open("d:\Downloads\wmr2015_annex4.csv", "rb")
    reader = csv.DictReader(fp)
    # for row in reader:
    #     country = row.get("Country/area", None)
    #     if country:
    #         print "\"%s\"," % country,
    # exit(0)

    country = None
    while True:
        try:
            row = reader.next()
        except StopIteration:
            break
        country = row.get("Country/area", None) or country
        country = country.strip()
        year = row.get("Year")
        if not year:
            continue
        irs_coverage = get_number(row.get("% IRS coverage"))
        irs_people = get_number(row.get("No. of people protected by IRS"))
        location_queryset = DimLocation.objects.filter(admin0=country)  # Uganda/Tororo and Viet Nam/Bihn Long
        if location_queryset.count() != 1:
            location_queryset = DimLocation.objects.filter(admin0=country, admin1=None, admin2=None, admin3=None)
        if location_queryset.count() == 1:
            pass
            # print location_queryset[0].id
        else:
            print "%s - unknown location (%s)" % (country, location_queryset.count())
            continue

        date_obj = DimDate.objects.filter(timestamp__year=int(year))[0]
        # print date_obj.id

        source = DimSource.objects.get_or_create(
            source="World Malaria Report 2015 Annex 4",
            file_uid="gh93h9255",
        )[0]
        if irs_people is not None and irs_coverage is not None:

            print location_queryset[0], year, irs_coverage, irs_people
            FactWmrIrsOprtnlCvrg.objects.create(
                # id = models.IntegerField(primary_key=True)
                nmbr_protected_irs=irs_people,
                pcnt_irs_cvrg=irs_coverage,
                location_key=location_queryset[0],
                date_key=date_obj,
                end_date_key=date_obj,
                user_key_id=1,
                source_key=source,
            )

        # print country, year, itn_coverage, itn_sold, llin_sold, llin_itn_sold
