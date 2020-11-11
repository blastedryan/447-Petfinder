from tests.webtests import WebTests
from selenium.webdriver.support.ui import Select
import time
import os
import json

class BreedValidation(WebTests):
    # Goes to a specific pet page, enters a breed, submits the search, and retrieves the search from a json
    # Returns a dictionary of the search query
    def breed_send(self, button, breed):
        self.driver.get(self.htmlPath)
        time.sleep(2)
        self.driver.find_element_by_id(button).click()
        time.sleep(2)
        self.driver.find_element_by_id('headingOne').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='breed']").send_keys(breed)
        time.sleep(2)
        self.driver.find_element_by_id('headingTwelve').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='location']").send_keys("Baltimore, MD")
        submit = self.driver.find_element_by_xpath("//input[@value='search']")
        submit.click()
        time.sleep(5)
        with open('test_breed_search.json', 'r') as fp:
            search = json.load(fp)
        return search

    def test_dog(self):
        search = self.breed_send('dog_button', 'American Bulldog')
        assert search['breed'] == ['American Bulldog']
        search = self.breed_send('dog_button', 'hello')
        assert search['breed'] == 'NOT FOUND'

    # def test_cat(self):
    #     search = self.breed_send('cat_button', 'Toyger')
    #     assert search['breed'] == ['Toyger']
    #     search = self.breed_send('cat_button', 'hello')
    #     assert search['breed'] == 'NOT FOUND'


