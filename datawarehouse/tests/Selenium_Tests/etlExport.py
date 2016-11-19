# This file is part of the VecNet Data Warehouse Browser.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/vecnet/dw
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/

import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class EtlExport(unittest.TestCase):
    # TODO Add class docstring
    # TODO Add method docstring(s)
    test_type = 'funct'
    browser = 'firefox'
    localhost = 'http://localhost:8000'

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_etl_export(self):
        driver = self.driver
        driver.get(self.base_url + "/datawarehouse/etl/upload")
        driver.find_element_by_id("id_upload-inputFile").clear()
        driver.find_element_by_id("id_upload-inputFile").send_keys(
            "/opt/VECNet_env/vnetsource/datawarehouse/Selenium/Selenium Tests/household_data2.csv")
        driver.find_element_by_css_selector("button.right.btn").click()
        # find the select box and its options
        select = Select(driver.find_element_by_id("id_selectTable-tables"))
        options = select.options
        print options
        driver.find_element_by_css_selector("button.right.btn").click()
        driver.find_element_by_id("addToMap").click()
        driver.find_element_by_css_selector("button.right.btn").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
