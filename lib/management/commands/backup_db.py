# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.core.management.base import BaseCommand, CommandError
from django import db
from django.conf import settings
import shutil
import time
import os
import subprocess


def backup(label, user):
    """ If postgresql is used as database engine, this function calls pg_dump command
    :param label:
    :param user:
    :return:
    """
    engine = db.connections.databases["default"]["ENGINE"]

    if engine == "django.db.backends.sqlite3":
        filename = label + "-" + str(user) + time.strftime("-%Y-%m-%d_%H%M%S") + ".sqlite3"
        shutil.copyfile(db.connections.databases["default"]["NAME"],
                        os.path.join(settings.DATABASE_BACKUP_DIR, filename))

        return True, filename
    elif engine == "django.db.backends.postgresql_psycopg2" or engine == "django.db.backends.postgresql" \
            or engine == "django.contrib.gis.db.backends.postgis":

        # Note that SELECT permission for schema topology is required when using with postgis
        # Otherwise, pg_dump will fail:
        # pg_dump: [archiver (db)] query failed: ERROR:  permission denied for schema topology
        # pg_dump: [archiver (db)] query was: LOCK TABLE topology.topology IN ACCESS SHARE MODE

        # How to fix:
        # sudo -u postgres /usr/pgsql-9.3/bin/psql -d dw2 -c "GRANT ALL PRIVILEGES ON SCHEMA topology to dw;"
        # sudo -u postgres /usr/pgsql-9.3/bin/psql -d dw2 -c "GRANT ALL PRIVILEGES ON ALL TABLES in SCHEMA topology to dw;"


        filename = label + "-" + str(user) + time.strftime("-%Y-%m-%d_%H%M%S") + ".pg_dump"

        # Create directory if does not exist first
        try:
            os.makedirs(settings.DATABASE_BACKUP_DIR)
        except OSError:
            if not os.path.isdir(settings.DATABASE_BACKUP_DIR):
                raise

        filename = os.path.join(settings.DATABASE_BACKUP_DIR, filename)
        command = "pg_dump -h %s -p %s -U %s -F c -f '%s' %s" % \
                  (db.connections.databases["default"]["HOST"],
                   str(db.connections.databases["default"].get("PORT", "5432")),
                   db.connections.databases["default"]["USER"],
                   filename,
                   db.connections.databases["default"]["NAME"]
                   )
        ret_code = subprocess.call(command,
                                   env=dict(os.environ, PGPASSWORD=db.connections.databases["default"]["PASSWORD"]),
                                   shell=True)
        if ret_code != 0:
            return False, "pg_dump command failed, error code %s" % ret_code

        return True, filename
    else:
        return False, "Engine %s is not supported" % engine


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting %s database backup" % db.connections.databases["default"]["NAME"])
        result, message = backup("Backup", os.environ.get("USER", ""))
        if result:
            print("Backup complete, filename %s" % message)
        else:
            # If a management command is called from code through call_command,
            # it's up to you to catch the exception when needed.
            raise CommandError(message)
