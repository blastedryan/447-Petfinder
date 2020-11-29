from tests.webtests import WebTests
from selenium.webdriver.support.ui import Select
import time
import os
import json


class UpdatingMap(WebTests):

    def test_search(self):
        self.driver.get(self.htmlPath)
        time.sleep(2)
        self.driver.find_element_by_id("dog_button").click()
        time.sleep(2)
        self.driver.find_element_by_id('headingOne').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='breed']").send_keys("Boxer")
        time.sleep(2)
        #self.driver.find_element_by_id('headingTwelve').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Baltimore, MD")

        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()

        time.sleep(10)
        
        self.driver.find_element_by_id('headingOne').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='breed']").send_keys("Pug")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Baltimore, MD")

        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()

        time.sleep(10)
