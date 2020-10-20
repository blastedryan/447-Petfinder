import unittest
import time
from selenium import webdriver
driverPath = webdriver.Chrome('')
htmlPath = ''
class HTMLTest(unittest.TestCase):
    def test_web_bones(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(3)
        self.driver.find_element_by_tag_name("input")
        time.sleep(3)
        self.driver.find_element_by_tag_name("label")
        time.sleep(3)
        self.driver.find_element_by_tag_name("button")