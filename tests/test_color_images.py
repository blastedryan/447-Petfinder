#This tests just makes sure all the images for the color section are in and that the buttons are buttons are larger allowing the images to be
#easier seen
import time
import unittest
from selenium import webdriver
from tests.webtests import WebTests
driverPath = webdriver.Chrome("C:\\Users\\Owner\\Desktop\\Chromedriver\\chromedriver.exe")
htmlPath = 'http://127.0.0.1:8000/petfinder'

class TestColor(unittest.TestCase):
    #first test the dog section
    def testDog(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(1)
        testDog = self.driver.find_element_by_id('dog_button')
        testDog.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(5)
        #click down on two buttons just to make sure they still work properly
        testClick = self.driver.find_element_by_id('black_dog_button')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('sable_dog_button')
        testClick.click()
        time.sleep(2)
    #Cats
    def testCat(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(1)
        testCat = self.driver.find_element_by_id('cat_button')
        testCat.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(5)
        #make sure the buttons still work properly
        testClick = self.driver.find_element_by_id('buff_cat_button')
        testClick.click()
        time.sleep(2)
        testClickTwo = self.driver.find_element_by_id('cream_cat_button')
        testClickTwo.click()
        time.sleep(2)
        testClick.click()
        time.sleep(3)
    #Barnyard Animals
    def testBarn(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(1)
        testBarn = self.driver.find_element_by_id('barn_button')
        testBarn.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(5)
        #make sure the buttons still work properly
        testClick = self.driver.find_element_by_id('black_white_barn_button')
        testClick.click()
        time.sleep(2)
        testClickTwo = self.driver.find_element_by_id('brindle_barn_button')
        testClickTwo.click()
        time.sleep(2)
    #Small and Furry Animals
    def testFurry(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(1)
        testFurry = self.driver.find_element_by_id('furry_button')
        testFurry.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(5)
        #make sure the buttons still work properly
        testClick = self.driver.find_element_by_id('black_furry_button')
        testClick.click()
        time.sleep(2)
        testClickTwo = self.driver.find_element_by_id('white_furry_button')
        testClickTwo.click()
        time.sleep(2)
    #Reptiles,Fish, Etc.
    def testScale(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(1)
        testScale = self.driver.find_element_by_id('scale_button')
        testScale.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(5)
        #make sure the buttons still work properly
        testClick = self.driver.find_element_by_id('brown_scale_button')
        testClick.click()
        time.sleep(2)
        testClickTwo = self.driver.find_element_by_id('orange_scale_button')
        testClickTwo.click()
        time.sleep(2)
        testClick.click()
        time.sleep(3)
    #horse
    def testHorse(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(1)
        testHorse = self.driver.find_element_by_id('horse_button')
        testHorse.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(5)
        #make sure the buttons still work properly
        testClick = self.driver.find_element_by_id('paint_horse_button')
        testClick.click()
        time.sleep(2)
        testClickTwo = self.driver.find_element_by_id('red_roan_horse_button')
        testClickTwo.click()
        time.sleep(4)
        testClickTwo.click()
        time.sleep(2)
    #rabbits
    def testRabbits(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(1)
        testRabbit = self.driver.find_element_by_id('rabbit_button')
        testRabbit.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(5)
        #make sure the buttons still work properly
        testClick = self.driver.find_element_by_id('orange_red_rabbit_button')
        testClick.click()
        time.sleep(2)
        testClickTwo = self.driver.find_element_by_id('sable_rabbit_button')
        testClickTwo.click()
        time.sleep(2)