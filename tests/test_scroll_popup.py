from tests.webtests import WebTests
from selenium.webdriver.support.ui import Select
import time
import os
import json
from selenium.webdriver import ActionChains


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
        self.driver.find_element_by_id('headingFour').click()
        time.sleep(2)
        self.driver.find_element_by_id('female_dog_button').click()
        
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Baltimore, MD")

        time.sleep(2)
        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()
        
        action = ActionChains(self.driver)
        map_elm = self.driver.find_element_by_id('map')
        action.move_to_element(map_elm).perform()

        time.sleep(10)

