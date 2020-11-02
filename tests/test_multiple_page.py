import time
import unittest
from selenium import webdriver
from tests.webtests import WebTests
driverPath = webdriver.Chrome("C:\\Users\\Owner\\Desktop\\Chromedriver\\chromedriver.exe")
#htmlPath = "C:\\Users\\Owner\\PycharmProjects\\447-Petfinder\\petsite\\petfinder\\templates\\petfinder\\HomePage.html"
htmlPath = 'http://127.0.0.1:8000/petfinder'
class TestHome(unittest.TestCase):
    def test_Open(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(3)
    def test_Dog(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testDog = self.driver.find_element_by_id('dog_button')
        testDog.click()
        time.sleep(3)
        testClick = self.driver.find_element_by_id('headingOne')
        testClick.click()
        time.sleep(3)
    def test_Cat(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testCat = self.driver.find_element_by_id('cat_button')
        testCat.click()
        time.sleep(3)
        testClick = self.driver.find_element_by_id('headingFour')
        testClick.click()
        time.sleep(3)

    def test_Bird(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testBird = self.driver.find_element_by_id('bird_button')
        testBird.click()
        time.sleep(3)
        testClick = self.driver.find_element_by_id('headingThree')
        testClick.click()
        time.sleep(3)
    def test_Reptile(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testReptile = self.driver.find_element_by_id('scale_button')
        testReptile.click()
        time.sleep(3)
        testClick = self.driver.find_element_by_id('headingSix')
        testClick.click()
        time.sleep(3)
    def test_Rabbit(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testRabbit = self.driver.find_element_by_id('rabbit_button')
        testRabbit.click()
        time.sleep(3)
        testClick = self.driver.find_element_by_id('headingNine')
        testClick.click()
        time.sleep(3)