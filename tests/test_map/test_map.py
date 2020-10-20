import unittest
import time
from selenium import webdriver

DRIVER_PATH = "/Users/monalisaraf/Downloads/chromedriver"
URL = 'file:///Users/monalisaraf/Petfinder/447-Petfinder/tests/Petfinder_style.html'


driver = webdriver.Chrome(DRIVER_PATH)
driver.get(URL)

