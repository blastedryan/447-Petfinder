# 447-Petfinder

## Installing

### Install Python
Go to the [Python website](https://www.python.org/downloads/) and install Python **3.7** or **3.8**   

**3.9 does not work!**

### Install Dependencies
Type `pip install -r requirements.txt` to install other dependencies

### Retrieving MapBox API Key
In order for the map to render, you must use the MapBox API key that is found in our team's Google Drive. Upon retrieving the key, insert the key on line 267, `mapboxgl.accessToken ='<insert key here>'`. Only after updating the key will the map become visible. In upcoming releases, a more secure method of key encryption will be available.

## Opening Site
Open your console and navigate to the directory.

Navigate into the folder petsite.

Run `python manage.py migrate` if it is your first time running the site.

Run `python manage.py runserver` or `py manage.py runserver`

Go to your browser and put in the address `http://127.0.0.1:8000/petfinder`

## Running Tests

Set up new environment variables: PETFINDER_KEY , PETFINDER_SECRET_KEY , PETSITE_SECRET_KEY
The values for the variables can be found in the google drive folder.

#### Instructions for setting up environment variables in windows 
https://www.computerhope.com/issues/ch000549.htm

#### Instructions for setting up environment variables in mac
1. Open terminal
2. Run “nano ~/.bash_profile”
3. Scroll to the bottom of the file and add these two lines, replacing ``<key>`` and ``<secret key>`` with the key you're given

    * `export PETFINDER_KEY=<key>`
    * `export PETFINDER_SECRET_KEY=<secret key>`
    * `export PETSITE_SECRET_KEY=<secret key>`

4. Type “CONTROL+X”, then “Y” and “enter”
5. Restart your ide or terminal and the variables should be setup properly

Using Pytest either in Pycharm or Terminal you can run every test in the file tests/test_query.py or individual tests. 

Each test is its own function inside of the file starting with the word ‘test’. 

Information on how to use Pytest in Pycharm can be found here: https://www.jetbrains.com/help/pycharm/pytest.html#enable-pytest and 
Pytest documentation for terminal commands can be found here: https://docs.pytest.org/en/stable/usage.html.

The current supported tests, test the basic functionality of retrieving petfinder data. As we add the functionality for searching for specific criteria in future iterations, other tests in the suite will be added, testing said criteria 
(ie. a test exhausting the location formats when we work on a user story involving location)

#### Running Selenium Tests 
1. Open terminal
2. Go into the tests directory.
3. To run the selenium tests you must first install selenium by going to https://www.selenium.dev/downloads/. 
4. Then you must install a chrome webdriver from https://chromedriver.chromium.org/downloads. (Make sure it is compatible
with your version of Chrome ie. 87, 86, or 85) 
5. Once that is done you must put the path to webdriver and html (tests/Petfinder_template.html) into the global 
variables driverPath and htmlPath. You can find the html path easily by opening the file in chrome  and copying the link
at the top.
6. Once that is done you can just run tests/testStyle.py with pytest and it should open up a web browser with the html link displayed on it. 
The current tests just test if the web page opens correctly and if the accordion table acts appropriately.

In order to test the MapBox API, follow the same instructions with the python file in tests/test_map. The map should render at the bottom of the web page. You should be able to hover your mouse over two markers, and you should see windows popup over those markers with information of two dogs. This is purely for Iteration 1 testing purposes, as later iterations will have more markers on the map, based on search results. Before testing, you must first insert the MapBox API Key, as specified in the "Retrieving MapBox API Key" section above.
