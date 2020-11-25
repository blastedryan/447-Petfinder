from tests.webtests import WebTests
from selenium.webdriver.support.ui import Select
import time
import os
import json


class MapCenter(WebTests):
    '''
    If this test is successful, after the first search the map should be centered on Baltimore, MD and the second
    search is centered on Seattle, WA
    '''
    def test_map_center(self):
        self.driver.get(self.htmlPath)
        time.sleep(2)
        self.driver.find_element_by_id("dog_button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Baltimore, MD")

        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()

        time.sleep(10)

        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Seattle, WA")

        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()

        time.sleep(10)
