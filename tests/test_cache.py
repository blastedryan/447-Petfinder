from petsite.petfinder_api.query import authenticate, key, secret_key
from petsite.cache.cache import find_pets_with_cache
from pandas import DataFrame
from django.core.cache import cache
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'petsite.petsite.settings'

pf = authenticate(key, secret_key)
num_results = 50  # number of results we want


def test_petfind_with_cache():
    cache.set('test','123')
    assert cache.get('test') == '123'
    cache.clear()  # make sure we start with an empty cache
    pets = find_pets_with_cache(pf)
    cache_result = cache.get('default')
    assert isinstance(cache_result, DataFrame)
    assert cache_result.shape[0] == num_results
    assert cache_result.equals(pets)

def test_remove_dupe():
    cache.clear()  # make sure we start with an empty cache
    pets = find_pets_with_cache(pf)
    find_pets_with_cache(pf)
    cache_result = cache.get('default')
    assert pets.equals(cache_result)

def test_petfind_complex_with_cache():
    cache.clear()
    pets = find_pets_with_cache(pf, animal_type='dog')
    cache_result = cache.get('default')
    assert isinstance(pets, DataFrame)
    assert cache_result['animal_type'][0] == 'dog'
    find_pets_with_cache(pf)
    pets2 = find_pets_with_cache(pf, animal_type='dog')
    assert pets.equals(pets2)
