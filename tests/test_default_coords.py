from petsite.petfinder_api.query import find_pets, authenticate, key, secret_key
from pandas import DataFrame, Series, isnull
import pytest
from petpy.exceptions import PetfinderInvalidCredentials
import json
import os

pf = authenticate(key, secret_key)

# Tests if missing lat long coords are filled in with users location
def test_default_coords():
    # Originally NaN values for rows with BC as a province/state
    pets, _ = find_pets(pf, location='Vancouver, BC', distance = 100)
    print(pets[['contact.address.lat', 'contact.address.long', 'contact.address.state']])
    assert pets[isnull(pets['contact.address.lat'])].shape[0] == 0
