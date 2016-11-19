# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/


import unittest

import cubes

from datawarehouse.cubes_config import engine, dwmodel
from datawarehouse.models import fact_prefix, dimension_prefix


class CubesTestCase(unittest.TestCase):
    def test_model(self):
        """
        Making sure the model can be loaded and is valid
        """
        filename = 'datawarehouse/fixtures/datawarehouse.json'
        model = cubes.load_model(filename)
        self.assertIsInstance(model, cubes.model.Model)

    def test_cubes(self):
        """
        Testing that each cube can be instantiated
        Testing that facts in each cube can be called

        This will insure that you can aggregate and get
        raw data from each of the cubes in the model used
        by the datawarehouse.  This should work when you
        change schema and add when you add cubes.
        """
        filename = 'datawarehouse/fixtures/datawarehouse.json'
        workspace = cubes.create_workspace('sql', dwmodel, engine=engine, fact_prefix=fact_prefix,
                                           dimension_prefix=dimension_prefix)
        for c_key, c_name in dwmodel.cubes.iteritems():
            cube = dwmodel.cube(c_name)
            self.assertIsInstance(cube, cubes.model.Cube)
            try:
                # If mapping is explicitly defined, grab the explicit mapping for key
                cube.key = cube.mappings['id']
            except (TypeError, KeyError):
                # Otherwise either no mappings are listed or a mapping for 'id' does not exist
                pass
            try:
                browser = workspace.browser(cube)
            except Exception as error:
                print "Cube: " + c_key + " Failed"
                print error
                assert False
            self.assertIsInstance(browser, cubes.backends.sql.star.SnowflakeBrowser)
            cell = cubes.Cell(cube)
            try:
                facts = browser.facts(cell)
            except Exception as error:
                print "Cube: " + c_key + " Failed"
                print error
                assert False
            assert True
            print "Cube: " + c_key + " Passed"
