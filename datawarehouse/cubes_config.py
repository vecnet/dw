# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from cubes import load_model
from django.db import connections
from django.conf import settings

# Setup the connections to the DB for cubes/sqlalchemy
# engine = connection requirement for cubes/sqlalchemy
engine = create_engine(
    'postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s' % connections['default'].settings_dict)

# Session = required when querying the database from sqlalchemy
Session = scoped_session(sessionmaker(bind=engine))

path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.sep.join(path.split(os.path.sep)[:-2]) + os.path.sep

# Load the warehouse model from datawarehouse.json
# dwmodel = load_model(os.path.join(settings.PROJECT_ROOT, 'datawarehouse/fixtures/datawarehouse_mk2.json'))
if os.name == "nt":
    # load_model won't accept full path on Windows, as it interprets c:// as protocol (like http:// etc)
    dwmodel = load_model('datawarehouse/fixtures/datawarehouse_mk2.json')
else:
    dwmodel = load_model(os.path.join(settings.PROJECT_ROOT, 'datawarehouse/fixtures/datawarehouse_mk2.json'))
