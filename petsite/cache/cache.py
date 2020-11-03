"""
This is a cache database that holds all query results in the past 24 hours
This is basically my first time writing python code so don't expect anything out of it
"""
import os
from django.core.cache import cache
from petfinder_api.query import find_pets, authenticate, key, secret_key
from petpy.api import Petfinder

num_results = 50  # number of results we want
os.environ['DJANGO_SETTINGS_MODULE'] = 'petsite.petsite.settings'

def find_pets_with_cache(pf: Petfinder, location=None, animal_type=None, breed=None, size=None, gender=None, age=None, color=None,
              coat=None, org_name=None, distance=None, name=None, good_with=[], house_trained=None, special_needs=None,
              sort=None):
    # if cache is empty fill with query
    if cache.get('default') is None:
        pets, _ = find_pets(pf, location, animal_type, breed, size, gender, age, color,
              coat, org_name, distance, name, good_with, house_trained, special_needs, sort)
        cache.set('default',pets)
    else:
        pets = cache.get('default')
        # search cache

        if animal_type is not None and pets.shape[0] > num_results:
            pets = pets.where(pets['animal_type'] == animal_type)

        # other attributes...

        # if there are not enough results in the cache, run query and cache results
        # if pets.shape[0] < num_results:
        #     pets, _ = find_pets(pf, location, animal_type, breed, size, gender, age, color,
        #       coat, org_name, distance, name, good_with, house_trained, special_needs, sort)
        #     temp = cache.get('default')
        #     pets = pets.append(temp,ignore_index=True)
        #     pets = pets.drop_duplicates()
        #     cache.set('default', pets)
        # else:
        #     # if more results than wanted, drop bottom values until there are proper number of results
        #     while pets.shape[0] != num_results:
        #         pets.drop(pets.index[num_results])
    return pets
