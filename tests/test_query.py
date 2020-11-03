from petfinder_api.query import find_pets, authenticate, key, secret_key
from pandas import DataFrame
import pytest
from petpy.exceptions import PetfinderInvalidCredentials
import json
import os

pf = authenticate(key, secret_key)
MAX_PETS = 100

def test_authenticate_success():
    pf = authenticate(key, secret_key)
    assert isinstance(pf._auth, str)


def test_authenticate_fail():
    with pytest.raises(PetfinderInvalidCredentials):
        pf = authenticate('hello', 'hello')

def test_petfind():
    pets = find_pets(pf)
    assert isinstance(pets, DataFrame) and pets.shape[0] == MAX_PETS


def test_petfind_complex():
    pets = find_pets(pf, location='Baltimore, MD', animal_type='dog', breed='beagle', distance=50, name='Bayla',
                     age='young', size='small', gender='female', coat='short')
    assert isinstance(pets, DataFrame) and pets['name'][0] == 'Bayla'


def test_petfind_goodwith():
    pets = find_pets(pf, good_with=['cat', 'dog'])
    assert all(pets['environment.cats']) and all(pets['environment.dogs'])

def test_petfind_json_age():
    search_json_path = os.path.join(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))), 'petsite/search.json')
    with open(search_json_path, 'r') as fp:
        search = json.load(fp)

    pets = find_pets(pf, age=search['age'])

    assert isinstance(search, dict)
    assert isinstance(pets, DataFrame)







