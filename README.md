# 447-Petfinder

## Installing

### Install Python
Go to the [Python website](https://www.python.org/downloads/) and install Python **3.7** or **3.8**   

**3.9 does not work!**

### Install Dependencies
Type `pip install -r requirements.txt` to install other dependencies

### Retrieving MapBox API Key
In order for the map to render, you must use the MapBox API key that is found in our team's Google Drive. Upon retrieving the key, insert the key on line 267, mapboxgl.accessToken ='<insert key here>'. Only after updating the key will the map become visible. In upcoming releases, a more secure method of key encryption will be available.

## Opening Site
Open your console and navigate to the directory.

Navigate into the folder petsite.

Run `python manage.py migrate` if it is your first time running the site.

Run `python manage.py runserver` or `py manage.py runserver`

Go to your browser and put in the address `http://127.0.0.1:8000/petfinder`

## Running Tests

Set up two new environment variables


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
