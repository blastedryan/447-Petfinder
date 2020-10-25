"""
Filename: query.py
Author: Nicholas Potteiger
Description: This is the code for the main interface for accessing specific animals from Petfinder.

Credit goes to https://github.com/aschleg/petpy for Petfinder Python Wrapper
"""
import os
from petpy.api import Petfinder
from pandas import Series


key = os.environ.get('PETFINDER_KEY')
secret_key = os.environ.get('PETFINDER_SECRET_KEY')

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
    # Create a boolean list of values related to what the animal is good_with
    actual_compatible = [None, None, None]
    possible_compatible = ['cat','dog', 'children']
    if len(good_with) != 0:
        for i in range(len(possible_compatible)):
            if possible_compatible[i] in good_with:
                actual_compatible[i] = True

    org_ids = None
    if org_name is not None:
        """
        If the org name is not found in the database, meaning a possible faulty search occurred, slice words from the
        front of the org name until either organization ids are returned or none are. The organization ids returned will 
        be used to search for pets within those organizations.
        """
        tmp_name = org_name
        org_ids = __get_org_ids(pf, orgname=tmp_name)
        if not isinstance(org_ids, Series):
            length = len(tmp_name.split()) - 1
            org_bool = False
            for i in range(length):
                tmp_name = tmp_name.split(' ', 1)[1]
                org_ids = __get_org_ids(pf, orgname=tmp_name)
                if isinstance(org_ids, Series):
                    org_bool = True
                    break

        if not org_bool:
            return 0
    try:
        pets = pf.animals(location=location, animal_type=animal_type, breed=breed, size=size, gender=gender, age=age,
                      color=color, coat=coat, distance=distance, name=name, good_with_cats=actual_compatible[0],
                      good_with_dogs=actual_compatible[1], good_with_children=actual_compatible[2],
                      results_per_page=50, organization_id=org_ids, pages=1, sort=sort, return_df=True)
    except:
        return 0

    if house_trained is not None:
        pets = pets.loc[pets['attributes.house_trained'] == True]
    if special_needs is not None:
        pets = pets.loc[pets['attributes.special_needs'] == True]
    return pets

"""
Returns a pandas dataframe of organization ids to be used in find_pets() to find pets based on organizations
Input: A string representing partial or full organization name
Output: The organization ids associated with the string or 0 if no org could be found / error occurred

The output can fail depending on the string inputted even if the organization is in a database. 

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
