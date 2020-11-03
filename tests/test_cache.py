from petfinder_api.query import authenticate, key, secret_key
from petfinder_api.cache import find_pets_with_cache
from pandas import DataFrame
from django.core.cache import cache

pf = authenticate(key, secret_key)
num_results = 100  # number of results we want


def test_petfind_with_cache():
    cache.set('test','123')
    print(cache.get('test'))

    cache.clear()  # make sure we start with an empty cache
    pets = find_pets_with_cache(pf)
    cache_result = cache.get('default')
    assert isinstance(cache_result, DataFrame)
    assert cache_result.shape[0] == num_results
    assert cache_result == pets


def test_petfind_complex_with_cache():
    cache.clear()
    pets = find_pets_with_cache(pf, location='Baltimore, MD', animal_type='dog', breed='beagle', distance=50,
                                name='Bayla',
                                age='young', size='small', gender='female', coat='short')
    cache_result = cache.get('default')
    assert isinstance(pets, DataFrame)
    assert cache_result['name'][0] == 'Bayla'
    find_pets_with_cache(pf, location='Baltimore, MD', animal_type='dog', breed='beagle', distance=50,
                         name='John', age='young', size='small', gender='female', coat='short')
    pets2 = find_pets_with_cache(pf, location='Baltimore, MD', animal_type='dog', breed='beagle', distance=50,
                                 name='Bayla', age='young', size='small', gender='female', coat='short')
    assert pets == pets2
