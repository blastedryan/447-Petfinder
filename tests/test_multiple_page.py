#Note that to run this test you must first run python manage.py runserver like you would if you were trying to run the webapp
#This is becuase this test was made mainly to test the functionality of  HomePage.html wtih the Django framework
#The links used for these tests will not work if you try to run them by themselves
import time
import unittest
from selenium import webdriver
from tests.webtests import WebTests
driverPath = webdriver.Chrome("C:\\Users\\Owner\\Desktop\\Chromedriver\\chromedriver.exe")
#htmlPath = "C:\\Users\\Owner\\PycharmProjects\\447-Petfinder\\petsite\\petfinder\\templates\\petfinder\\HomePage.html"
htmlPath = 'http://127.0.0.1:8000/petfinder'
#This Just tests to see if the home page opens
class TestHome(unittest.TestCase):
    def test_Open(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        time.sleep(3)
    #This tests to see if the dog button will correctly link to the dog petfinder page
    def test_Dog(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testDog = self.driver.find_element_by_id('dog_button')
        testDog.click()
        time.sleep(3)
        #just a click to make sure the accordion can still be clicked
        testClick = self.driver.find_element_by_id('headingOne')
        testClick.click()
        time.sleep(3)
    #This tests to see if the cat button will correctly link to the cat petfinder page
    def test_Cat(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testCat = self.driver.find_element_by_id('cat_button')
        testCat.click()
        time.sleep(3)
        #Make sure the accordion still works
        testClick = self.driver.find_element_by_id('headingFour')
        testClick.click()
        time.sleep(3)
    #This tests to see if the bird button will correctly link to the bird petfinder page
    def test_Bird(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testBird = self.driver.find_element_by_id('bird_button')
        testBird.click()
        time.sleep(3)
        #Make sure the accordion still works
        testClick = self.driver.find_element_by_id('headingThree')
        testClick.click()
        time.sleep(3)
    #This tests to see if the scale button will correctly link to the fish,reptile, and amphibian page
    def test_Reptile(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testReptile = self.driver.find_element_by_id('scale_button')
        testReptile.click()
        time.sleep(3)
        #Make sure the accordion still works
        testClick = self.driver.find_element_by_id('headingSix')
        testClick.click()
        time.sleep(3)
    #This tests to see if the rabbit button will correctly link to the rabbit page
    def test_Rabbit(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testRabbit = self.driver.find_element_by_id('rabbit_button')
        testRabbit.click()
        time.sleep(3)
        #Make sure the accordion still works
        testClick = self.driver.find_element_by_id('headingNine')
        testClick.click()
        time.sleep(3)