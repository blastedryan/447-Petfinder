'''
This is the cache database that holds all query results in the past day
This is basically my first time writing python code so don't expect anything out of it
'''
from petpy.api import Petfinder
from django.core.cache import caches
from petfinder_api.query import find_pets, authenticate, key, secret_key

def find_pets_with_cache(pf: Petfinder, location=None, animal_type=None, breed=None, size=None, gender=None, age=None, color=None,
              coat=None, org_name=None, distance=None, name=None, good_with=[], house_trained=None, special_needs=None,
              sort=None):
    #if cache is empty fill with query
    if (cache.get('default')==None):
        pets = find_pets(pf, location, animal_type, breed, distance, name,age, size, gender, coat)
        cache.set('default',pets)

    else:

        pets = find_pets(pf, location, animal_type, breed, distance, name, age, size, gender, coat)
        temp = cache.get('default')
        pets = pets.append(temp,ignore_index=True)
        pets = pets.drop_duplicates()
        cache.set('default', pets)
    return pets