from tests.webtests import WebTests
from selenium.webdriver.support.ui import Select
import time
import os
import json

class WebBones(WebTests):
    def test_web_bones(self):
        self.driver.get(self.htmlPath)
        self.driver.find_element_by_tag_name("input")
        self.driver.find_element_by_tag_name("label")
        self.driver.find_element_by_tag_name("button")

    
    def test_search(self):
        self.driver.get(self.htmlPath)
        self.driver.find_element_by_id('headingOne').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='breed']").send_keys("Boxer")


        time.sleep(2)
        self.driver.find_element_by_id('headingTwo').click()
        time.sleep(2)

        self.driver.find_element_by_id('young-btn').click()
        time.sleep(2)

        self.driver.find_element_by_id('headingThree').click()
        time.sleep(2)
        self.driver.find_element_by_id('btn-small').click()
        self.driver.find_element_by_id('btn-large').click()


        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()

        search_json_path = os.path.join(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))), 'petsite/search.json')
        with open('search.json', 'r') as fp:
            search = json.load(fp)

        assert search["breed"] == ["Boxer"]
        assert search["young"] == ['on']

        