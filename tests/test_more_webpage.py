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
        time.sleep(2)
        #just a click to make sure the accordion can still be clicked
        #opened all twelve to see if the images loaded
        testClick = self.driver.find_element_by_id('headingOne')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('headingTwo')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('headingThree')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('headingFour')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('headingFive')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('headingSix')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('headingEight')
        testClick.click()
        time.sleep(3)
        #This tests to see if the cat button will correctly link to the cat petfinder page
    def test_Cat(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testCat = self.driver.find_element_by_id('cat_button')
        testCat.click()
        time.sleep(3)
        #Make sure the accordion still works, opens the gender accoridon file
        testClick = self.driver.find_element_by_id('headingFour')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('female_cat_button')
        testClick.click()
        time.sleep(1)
        testClickTwo = self.driver.find_element_by_id('male_cat_button')
        testClickTwo.click()
        time.sleep(1)
        testClick.click()
        time.sleep(1)
    #This tests to see if the bird button will correctly link to the bird petfinder page
    def test_Bird(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testBird = self.driver.find_element_by_id('bird_button')
        testBird.click()
        time.sleep(2)
        #Make sure the accordion still works, opens the size accordion file
        testClick = self.driver.find_element_by_id('headingThree')
        testClick.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('medium_bird_button')
        testClick.click()
        time.sleep(1)
        testClickTwo = self.driver.find_element_by_id('xlarge_bird_button')
        testClickTwo.click()
        time.sleep(3)
        testClickTwo.click()
        time.sleep(1)

    #This tests to see if the scale button will correctly link to the fish,reptile, and amphibian page
    def test_Reptile(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testReptile = self.driver.find_element_by_id('scale_button')
        testReptile.click()
        time.sleep(3)
        #Make sure the accordion still works
        #opens the color accordion file
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('gray_scale_button')
        testClick.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('red_scale_button')
        testClick.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('yellow_scale_button')
        testClick.click()
        time.sleep(1)
        #make sure that after the current accordion file is closed that the checkboxes remain chcecked
        testClick = self.driver.find_element_by_id('headingFive')
        testClick.click()
        time.sleep(1)
        testClick = self.driver.find_element_by_id('headingSeven')
        testClick.click()
        time.sleep(2)
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
        #make sure the button clicks down
        testClick = self.driver.find_element_by_id('1_week_rabbit_button')
        testClick.click()
        time.sleep(2)
    def test_Barn(self):
        self.driver= driverPath
        self.driver.get(htmlPath)
        testBarn = self.driver.find_element_by_id('barn_button')
        testBarn.click()
        time.sleep(3)
        testClick = self.driver.find_element_by_id('headingOneandaHalf')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('cow_button')
        testClick.click()
        time.sleep(2)
        testClick.click()
        time.sleep(2)
    def test_Furry(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testFurry = self.driver.find_element_by_id('furry_button')
        testFurry.click()
        time.sleep(3)
        #open the care and behavior accordion file
        testClick = self.driver.find_element_by_id('headingEight')
        testClick.click()
        time.sleep(1)
        #click both buttons and the reclick the second to see if it then turns off
        testClick = self.driver.find_element_by_id('house_trained_furry_button')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('special_needs_furry_button')
        testClick.click()
        time.sleep(2)
        testClick.click()
        time.sleep(2)
    def test_Horse(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testHorse = self.driver.find_element_by_id('horse_button')
        testHorse.click()
        time.sleep(3)
        testClick = self.driver.find_element_by_id('headingFive')
        testClick.click()
        time.sleep(2)
        testClick = self.driver.find_element_by_id('good_with_dogs_horse_button')
        testClick.click()
        time.sleep(2)
        testClick.click()
        time.sleep(2)
class testFalseSearch(unittest.TestCase):
    def test_False(self):
        self.driver = driverPath
        self.driver.get(htmlPath)
        testFalse = self.driver.find_element_by_id('dog_button')
        testFalse.click()
        time.sleep(2)
        #This will test what happens if the user tries to search without entering their location. It should not send and display a message
        #That says "please fill out this field"
        testClick = self.driver.find_element_by_id('search_button')
        testClick.click()
        time.sleep(2)
        testSearch = self.driver.find_element_by_id('location')
        #After the location field is filled in it should search with no problem (Right now it'll just relod the page)
        testSearch.send_keys("Test")
        time.sleep(2)
        testClick.click()
        time.sleep(3)