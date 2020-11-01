import time
import unittest
from selenium import webdriver
from tests.webtests import WebTests

class TestHome(unittest.TestCase):
    def test_Dog(self):
        driverPath = webdriver.Chrome("C:\\Users\\Owner\\Desktop\\Chromedriver\\chromedriver.exe")

        time.sleep(5)