import unittest
import subprocess
import os
from selenium import webdriver

class WebTests(unittest.TestCase):
    def setUp(self):
        port = '8000'
        driverPath = '/Users/monalisaraf/Downloads/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        manage_py_path = os.path.join(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))), 'petsite/manage.py')
        self.process = subprocess.Popen(['python', manage_py_path , 'runserver', port])
        self.htmlPath = 'http://127.0.0.1:{}/petfinder'.format(port)
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    def tearDown(self):
        self.process.kill()
        self.driver.close()
