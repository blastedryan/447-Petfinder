from tests.webtests import WebTests
from selenium.webdriver.support.ui import Select
import time
import os
import json
import pathlib
class WebBones(WebTests):
    def test_web_bones(self):
        self.driver.get(self.htmlPath)
        self.driver.find_element_by_id("dog_button").click()
        self.driver.find_element_by_tag_name("input")
        self.driver.find_element_by_tag_name("label")
        self.driver.find_element_by_tag_name("button")

    
    def test_search(self):
        self.driver.get(self.htmlPath)
        self.driver.find_element_by_id("dog_button").click()
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
        time.sleep(2)

        self.driver.find_element_by_id('headingTwelve').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Baltimore, MD")


        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()

        

        parentdir = pathlib.Path(__file__).parent.absolute()

        search_json_path = parentdir / 'petsite/search.json'
        with open(parentdir / 'search.json', 'r') as fp:
            search = json.load(fp)

        time.sleep(3)
        assert search["breed"] == ["Boxer"]
        assert search["young"] == ['on']
        assert search ["location"] == ["Baltimore, MD"]

    
        # Make sure the search for the petfinder is formatted correctly
        with open(parentdir / 'petfind_query.json', 'r') as fp:
            petfind_query = json.load(fp)

        assert petfind_query["breed"] == 'Boxer'
        assert petfind_query["location"] == "Baltimore, MD"


        