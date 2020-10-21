import time
from tests.webtests import WebTests

class FirstTest(WebTests):
    def test_first_selenium_test(self):
        #See if it just opens the web page
        self.driver.get(self.htmlPath)
        time.sleep(3)
        #See if it opens the first accordian section
        testBreed = self.driver.find_element_by_id('headingOne')
        testBreed.click()
        time.sleep(1)
        #See if the accordian closes once you click it again
        testBreed.click()
        time.sleep(2)
        #See if it opens the second accoridan folder
        testAge = self.driver.find_element_by_id('headingTwo')
        testAge.click()
        time.sleep(2)
        #See if it opens the third accordian and closes the second
        testSize = self.driver.find_element_by_id('headingThree')
        testSize.click()
        time.sleep(2)
        #See if it opens the fourth accordian and closes the third
        testGender = self.driver.find_element_by_id('headingFour')
        testGender.click()
        time.sleep(2)
        #See if it opens the fifth accoridan and closes the fourth
        testGoodWith = self.driver.find_element_by_id('headingFive')
        testGoodWith.click()
        time.sleep(2)
        #See if it opens the sixth accordian and closes the fifth
        testCoat = self.driver.find_element_by_id('headingSix')
        testCoat.click()
        time.sleep(2)
        #See if it opens the seventh accordian and closes the sixth
        testColor = self.driver.find_element_by_id('headingSeven')
        testColor.click()
        time.sleep(2)
        #See if it opens the eighth accoriand and closes the seventh
        testCare = self.driver.find_element_by_id('headingEight')
        testCare.click()
        time.sleep(2)
        #See if it opens the ninth accordian and closes the eighth
        testDays = self.driver.find_element_by_id('headingNine')
        testDays.click()
        time.sleep(2)
        #See if it opens the tenth accoridan and closes the ninth
        testShelter = self.driver.find_element_by_id('headingTen')
        testShelter.click()
        time.sleep(2)
