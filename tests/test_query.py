from petfinder_api.query import find_pets, authenticate, key, secret_key
from pandas import DataFrame, Series
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


def test_petfind_location():
    # City, State
    loc1 = 'Baltimore, MD'
    loc1_pets, _ = find_pets(pf, location=loc1, distance=25)
    # Postal Code
    loc2 = '21250'
    loc2_pets, _ = find_pets(pf, location=loc2, distance=25)
    # lat, long
    loc3 = '39.258, -76.713'
    loc3_pets, _ = find_pets(pf, location=loc3, distance=25)

    assert isinstance(loc1_pets, DataFrame)
    assert Series(['contact.address.address', 'contact.address.lat', 'contact.address.long']). \
        isin(loc1_pets.columns).all()
    assert isinstance(loc2_pets, DataFrame)
    assert Series(['contact.address.address', 'contact.address.lat', 'contact.address.long']). \
        isin(loc2_pets.columns).all()
    assert isinstance(loc3_pets, DataFrame)
    assert Series(['contact.address.address', 'contact.address.lat', 'contact.address.long']). \
        isin(loc3_pets.columns).all()
