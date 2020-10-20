import unittest
import subprocess
import os
from selenium import webdriver
class WebTests(unittest.TestCase):
    def setUp(self):
        port = '8232'
        driverPath = '/Users/jordantroutman/Downloads/chromedriver'
        manage_py_path = os.path.join(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))), 'petsite/manage.py')
        self.process = subprocess.Popen(['python', manage_py_path , 'runserver', port])
        self.htmlPath = 'http://127.0.0.1:{}/petfinder'.format(port)
        self.driver = webdriver.Chrome(driverPath)

    def tearDown(self):
        self.process.kill()
        self.driver.close()
