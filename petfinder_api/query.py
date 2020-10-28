"""
Filename: query.py
Author: Nicholas Potteiger
Description: This is the code for the main interface for accessing specific animals from Petfinder.

Credit goes to https://github.com/aschleg/petpy for Petfinder Python Wrapper
"""
import os
from petpy.api import Petfinder
from geopy.geocoders import Nominatim
import numpy as np
from pandas import DataFrame

key = os.environ.get('PETFINDER_KEY')
secret_key = os.environ.get('PETFINDER_SECRET_KEY')
locator = Nominatim(user_agent='myGeocoder')

"""
Authenticates the credentials of the developer to utilize Petfinder API
"""


def authenticate(key_val, secret_key_val):
    pf = Petfinder(key=key_val, secret=secret_key_val)
    return pf


"""
Returns a pandas data-frame of pets based on certain parameters specified
The parameters used in this function have descriptions that can be found here for what formats are allowed:
https://petpy.readthedocs.io/en/latest/api.html#find-listed-animals-on-petfinder

The first parameter is the Petfinder object
org_name is a string representing the name or partial name of an organization
good_with is a list containing what the specified animal should be good with (ie. 'cat', 'dog', 'children')
house_trained is a boolean 
special_needs is a boolean

returns 0 on failure or if the pet/org could not be found

Currently only 100 pets max will be returned but in the future more can be returned based on the Map API implementation
"""


def find_pets(pf: Petfinder, location=None, animal_type=None, breed=None, size=None, gender=None, age=None, color=None,
              coat=None, org_name=None, distance=None, name=None, good_with=[], house_trained=None, special_needs=None,
              sort=None):
    actual_compatible = [None, None, None]
    possible_compatible = ['cat', 'dog', 'children']
    if len(good_with) != 0:
        for i in range(len(possible_compatible)):
            if possible_compatible[i] in good_with:
                actual_compatible[i] = True

    org_ids = None
    searches = 0
    if org_name is not None:
        """
        To do: Create a method that searches for the full name of an org. If the name cannot be found, slice the string
        and retry the search with the sliced string. Find the search result in the dataframe by checking name column
        value.
        """
        org_ids = __get_org_ids(pf, org_name)
        searches += 1
        if not org_ids:
            return 0, searches
    try:
        ret_pets = pf.animals(location=location, animal_type=animal_type, breed=breed, size=size, gender=gender,
                              age=age,
                              color=color, coat=coat, distance=distance, name=name, good_with_cats=actual_compatible[0],
                              good_with_dogs=actual_compatible[1], good_with_children=actual_compatible[2],
                              results_per_page=50, organization_id=org_ids, pages=1, sort=sort, return_df=True)
        searches += 1
    except:
        return 0, searches

    if house_trained is not None:
        ret_pets = ret_pets.loc[ret_pets['attributes.house_trained'] == True]
    if special_needs is not None:
        ret_pets = ret_pets.loc[ret_pets['attributes.special_needs'] == True]

    ret_pets = __add_coords_col(ret_pets)
    return ret_pets, searches


"""
Returns a pandas dataframe of organization ids to be used in find_pets() to find pets based on organizations
Input: A string representing partial or full organization name
Output: The organization ids associated with the string or 0 if no org could be found / error occurred

The output can fail depending on the string inputted even if the organization is in a database.
Will look further into the cause of this. An example 'UC Davis Dog and Cat Adoptions' can be found by searching the
string 'Davis Dog and Cat Adoptions' but fails to find it with the full string.

The only consistent output is when only one word is inputted
"""


def __get_org_ids(pf: Petfinder, orgname=None):
    try:
        orgs = pf.organizations(name=orgname, results_per_page=100, pages=1, return_df=True)
        # print(orgs['name'][0:5])
        # print(orgs.shape)
        return orgs['id']
    except:
        # print('Failed')
        return 0


'''
Returns a pandas dataframe with a combined address, lat, and long column added.
Input: A pandas dataframe of pets with address columns included
Output: A pandas dataframe with 'contact.address.address', 'contact.address.lat', and 'contact.address.long' columns 
        added or -1 on error

Optimized to only find lat and long of unique addresses and replicate the output to duplicates
'''


def __add_coords_col(pets: DataFrame):
    try:
        pets['contact.address.address'] = pets['contact.address.city'].fillna('') + ', ' + \
                                          pets['contact.address.state'].fillna('') + ', ' + \
                                          pets['contact.address.postcode'].fillna('')
        unique_addresses = pets['contact.address.address'].unique()
        location_list = np.array([locator.geocode(x) for x in unique_addresses], dtype=object)
        lat_long_tup = np.array(location_list[:, 1])
        for i in range(len(unique_addresses)):
            pets.loc[pets['contact.address.address'] == unique_addresses[i], ['contact.address.lat',
                                                                              'contact.address.long']] = \
                lat_long_tup[i][0], lat_long_tup[i][1]

        return pets
    except:
        return -1
