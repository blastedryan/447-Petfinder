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
from pandas import DataFrame, Series, concat, DataFrame
from geopy.extra.rate_limiter import RateLimiter
import numpy as np
# from functools import reduce
# from itertools import chain

key = os.environ.get('PETFINDER_KEY')
secret_key = os.environ.get('PETFINDER_SECRET_KEY')
locator = Nominatim(user_agent='myGeocoder')
geocode = RateLimiter(locator.geocode, min_delay_seconds=0.1)
MAX_PETS = 50

"""
Authenticates the credentials of the developer to utilize Petfinder API
"""


def authenticate(key_val, secret_key_val):
    pf = Petfinder(key=key_val, secret=secret_key_val)
    return pf


"""
Returns a tuple of a pandas data-frame of pets based on certain parameters specified and the number of API queries 
required to find that data.
The parameters used in this function have descriptions that can be found here for what formats are allowed:
https://petpy.readthedocs.io/en/latest/api.html#find-listed-animals-on-petfinder

The first parameter is the Petfinder object
org_name is a string representing the name or partial name of an organization
good_with is a list containing what the specified animal should be good with (ie. 'cat', 'dog', 'children')
house_trained is a boolean 
special_needs is a boolean

returns 0 on failure or if the pet/org could not be found

Currently only 50 pets max will be returned but in the future more can be returned based on the Map API implementation
"""


def find_pets(pf: Petfinder, location=None, animal_type=None, breed=None, size=None, gender=None, age=None, color=None,
              coat=None, org_name=None, distance=None, name=None, good_with=[], house_trained=None, special_needs=None,
              sort=None):
    # Create a boolean list of values related to what the animal is good_with
    actual_compatible = [None, None, None]
    possible_compatible = ['cat', 'dog', 'children']
    if len(good_with) != 0:
        for i in range(len(possible_compatible)):
            if possible_compatible[i] in good_with:
                actual_compatible[i] = True

    search_count = 0
    org_ids = None
    if org_name is not None:
        """
        If the org name is not found in the database, meaning a possible faulty search occurred, slice words from the
        front of the org name until either organization ids are returned or none are. The organization ids returned will 
        be used to search for pets within those organizations.
        """
        tmp_name = org_name
        org_ids = __get_org_ids(pf, orgname=tmp_name)
        search_count += 1
        if not isinstance(org_ids, Series):
            length = len(tmp_name.split()) - 1
            org_bool = False
            for i in range(length):
                tmp_name = tmp_name.split(' ', 1)[1]
                org_ids = __get_org_ids(pf, orgname=tmp_name)
                search_count += 1
                if isinstance(org_ids, Series):
                    org_bool = True
                    break

            if not org_bool:
                return 0, search_count

    # Check to see if animals exist for each org
    animals_in = False
    if isinstance(org_ids, Series):
        org_ids = org_ids.tolist()
    else:
        org_ids = [None]
    pets_list = []
    for i in range(len(org_ids)):
        try:
            pets: DataFrame = pf.animals(location=location, animal_type=animal_type, breed=breed, size=size, gender=gender,
                              age=age, color=color, coat=coat, distance=distance, name=name,
                              good_with_cats=actual_compatible[0], good_with_dogs=actual_compatible[1],
                              good_with_children=actual_compatible[2], results_per_page=50, organization_id=org_ids[i],
                              pages=1, sort=sort, return_df=True)
            if i == 0:
                pets_list = pets
            else:
                pets_list = pets_list.loc[:, ~pets_list.columns.duplicated()]
                pets = pets.loc[:, ~pets.columns.duplicated()]
                # Add pets from org i to total pets dataframe
                pets_list = concat([pets_list, pets], ignore_index=True, axis=0)
            # pets_list.append(pets)
            animals_in = True
            search_count += 1
        except KeyError:
            continue

    if not animals_in:
        return 0, search_count

    # list_of_dicts = [cur_df.T.to_dict().values() for cur_df in pets_list]
    # ret_pets = DataFrame(list(chain(*list_of_dicts)))
    ret_pets = pets_list

    if house_trained is not None:
        ret_pets = ret_pets.loc[ret_pets['attributes.house_trained'] == True]
    if special_needs is not None:
        ret_pets = ret_pets.loc[ret_pets['attributes.special_needs'] == True]

    ret_pets = __add_coords_col(ret_pets.head(n=MAX_PETS))
    return ret_pets, search_count


"""
Returns a pandas dataframe of organization ids to be used in find_pets() to find pets based on organizations
Input: A string representing partial or full organization name
Output: The organization ids associated with the string or 0 if no org could be found / error occurred

The output can fail depending on the string inputted even if the organization is in a database. 

The only consistent output is when only one word is inputted
"""


def __get_org_ids(pf: Petfinder, orgname=None):
    try:
        orgs = pf.organizations(name=orgname, results_per_page=10, pages=1, return_df=True)
        # print(orgs['name'][0:5])
        # print(orgs.shape)
        return orgs['id']
    except KeyError:
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
        location_list = np.array([geocode(x) for x in unique_addresses], dtype=object)
        lat_long_tup = location_list
        for i in range(len(unique_addresses)):
            if not (lat_long_tup[i] is None):
                pets.loc[pets['contact.address.address'] == unique_addresses[i], ['contact.address.lat',
                                                                              'contact.address.long']] = \
                lat_long_tup[i][1][0], lat_long_tup[i][1][1]
            else:
                pets.loc[pets['contact.address.address'] == unique_addresses[i], ['contact.address.lat',
                                                                                  'contact.address.long']] = \
                    np.NaN, np.NaN

        return pets
    except:
        return -1
