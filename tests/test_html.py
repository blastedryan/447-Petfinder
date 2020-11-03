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
        self.driver.find_element_by_xpath("//input[@name='breed']").send_keys("Golden Doodle")


        time.sleep(2)
        self.driver.find_element_by_id('headingTwo').click()
        time.sleep(2)
        select = Select(self.driver.find_element_by_xpath("//select[@name='age']"))
        select.select_by_visible_text('Young')

        time.sleep(2)
        self.driver.find_element_by_id('headingThree').click()
        time.sleep(2)
        self.driver.find_element_by_id('size_small').click()
        self.driver.find_element_by_id('size_large').click()


        submit = self.driver.find_element_by_id("search")
        submit.click()

        search_json_path = os.path.join(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))), 'petsite/search.json')
        with open('search.json', 'r') as fp:
            search = json.load(fp)

        assert search["breed"] == ["Golden Doodle"]
        assert search["age"] == ['young']
        assert set(search["size"]) == set(["small", "large"])

        