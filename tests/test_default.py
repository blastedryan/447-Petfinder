from petsite.petfinder_api.query import find_pets, authenticate, key, secret_key
from pandas import DataFrame, Series, isnull
import pytest


pf = authenticate(key, secret_key)

# Tests if missing lat long coords are filled in with users location
def test_default_coords():
    # Originally NaN values for rows with BC as a province/state
    pets, _ = find_pets(pf, location='Vancouver, BC', distance = 100)
    print(pets[['contact.address.lat', 'contact.address.long', 'contact.address.state']])
    assert isinstance(pets, DataFrame)
    assert pets[isnull(pets['contact.address.lat'])].shape[0] == 0

# Tests if NaN values for primary photo are replaced with 'default' string, preventing error
def test_default_image():
    # This should have a couple defaults in it but due to the way Petfinder selects the pets, you may get a
    # different set each time so if you don't see default replacing the NaN and just all links then you may want to
    # rerun this test again until you see it
    pets, _ = find_pets(pf, location='Baltimore, MD')
    print(pets['primary_photo_cropped.small'])
    assert isinstance(pets, DataFrame)
    assert pets[isnull(pets['primary_photo_cropped.small'])].shape[0] == 0