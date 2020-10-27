"""
Filename: query.py
Author: Nicholas Potteiger
Description: This is the code for the main interface for accessing specific animals from Petfinder.

Credit goes to https://github.com/aschleg/petpy for Petfinder Python Wrapper
"""
import os
from petpy.api import Petfinder
from pandas import Series, concat


key = os.environ.get('PETFINDER_KEY')
secret_key = os.environ.get('PETFINDER_SECRET_KEY')

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
    possible_compatible = ['cat','dog', 'children']
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
    for ids in org_ids:
        try:
            pets = pf.animals(location=location, animal_type=animal_type, breed=breed, size=size, gender=gender, age=age,
                          color=color, coat=coat, distance=distance, name=name, good_with_cats=actual_compatible[0],
                          good_with_dogs=actual_compatible[1], good_with_children=actual_compatible[2],
                          results_per_page=50, organization_id=ids, pages=1, sort=sort, return_df=True)
            pets_list.append(pets)
            animals_in = True
            search_count += 1
        except:
            continue

    if not animals_in:
        return 0, search_count

    # Combine all of the pets from the various orgs into one dataframe
    ret_pets = concat(pets_list)

    if house_trained is not None:
        ret_pets = ret_pets.loc[ret_pets['attributes.house_trained'] == True]
    if special_needs is not None:
        ret_pets = ret_pets.loc[ret_pets['attributes.special_needs'] == True]

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
    except:
        # print('Failed')
        return 0
