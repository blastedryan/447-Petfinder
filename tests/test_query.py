from petfinder_api.query import find_pets, authenticate, key, secret_key
from pandas import DataFrame
import pytest
from petpy.exceptions import PetfinderInvalidCredentials

pf = authenticate(key, secret_key)
MAX_PETS = 50

def test_authenticate_success():
    pf = authenticate(key, secret_key)
    assert isinstance(pf._auth, str)


def test_authenticate_fail():
    with pytest.raises(PetfinderInvalidCredentials):
        pf = authenticate('hello', 'hello')

def test_petfind():
    pets, _ = find_pets(pf)
    assert isinstance(pets, DataFrame) and pets.shape[0] == MAX_PETS


def test_petfind_complex():
    pets, _ = find_pets(pf, location='Baltimore, MD', animal_type='dog', breed='beagle', distance=50, name='Bayla',
                     age='young', size='small', gender='female', coat='short')
    assert isinstance(pets, DataFrame) and pets['name'][0] == 'Bayla'


def test_petfind_goodwith():
    pets, _ = find_pets(pf, good_with=['cat', 'dog'])
    assert all(pets['environment.cats']) and all(pets['environment.dogs'])

def test_petfind_orgname():
    # Single word organization should not need slicing
    org1 = 'BARC'
    org1_pets, _ = find_pets(pf, org_name=org1)
    # Casing should not matter
    org2 = 'barc'
    org2_pets, _ = find_pets(pf, org_name=org2)
    # This org will require slicing due to the API not finding the org based on the full name
    org3 = 'Adopt A Pup Animal Rescue'
    org3_pets, _ = find_pets(pf, org_name=org3)

    assert isinstance(org1_pets, DataFrame)
    assert isinstance(org2_pets, DataFrame)
    assert isinstance(org3_pets, DataFrame)
    assert org1_pets.shape == org2_pets.shape








