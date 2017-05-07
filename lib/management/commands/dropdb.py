# -*- coding: utf-8 -*-
#
# This file is part of the Django Stash project.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--database",
            dest="database",
            help="Name of the database to create"
        )

    def handle(self, *args, **options):
        """
        Create the specified database. 
        Example:
            python manage.py dropdb mydb
        """
        database = options["database"]
        psql_path = getattr(settings, "PSQL_PATH", "psql")
        cmd = [psql_path, "-c", "DROP DATABASE %s;" % database]
        ret_code = subprocess.call(cmd, shell=False)

        if ret_code != 0:
            print("Can't drop database, error code %s" % ret_code)
