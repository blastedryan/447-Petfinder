from tests.webtests import WebTests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import json
import unittest
driverPath = webdriver.Chrome("C:\\Users\\Owner\\Desktop\\Chromedriver\\chromedriver.exe")
htmlPath = 'http://127.0.0.1:8000/petfinder'
class WebBones(unittest.TestCase):

    def test_web_bones(self):
        self.driver =driverPath
        self.driver.get(htmlPath)
        self.driver.find_element_by_id("dog_button").click()
        self.driver.find_element_by_tag_name("input")
        self.driver.find_element_by_tag_name("label")
        self.driver.find_element_by_tag_name("button")

    
    def test_search(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        self.driver.find_element_by_id("dog_button").click()
        self.driver.find_element_by_id('headingOne').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='breed']").send_keys("Boxer")


        time.sleep(2)
        self.driver.find_element_by_id('headingTwo').click()
        time.sleep(2)

        self.driver.find_element_by_id('young_dog_button').click()
        time.sleep(2)

        self.driver.find_element_by_id('headingThree').click()
        time.sleep(2)
        self.driver.find_element_by_id('small_dog_button').click()
        self.driver.find_element_by_id('large_dog_button').click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Baltimore, MD")


        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()

        

        search_json_path = os.path.join(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))), 'petsite/search.json')
        with open('search.json', 'r') as fp:
            search = json.load(fp)

        time.sleep(3)
        assert search["breed"] == ["Boxer"]
        assert search["young"] == ['on']
        assert search ["location"] == ["Baltimore, MD"]

        