from query import find_pets, authenticate, key, secret_key
import pytest
import json
import pandas as pd


pf = authenticate(key, secret_key)

def test_geojson():

    pets, _ = find_pets(pf, location='Baltimore, MD', animal_type='dog', breed='beagle', distance=50, name='Bayla',
                        age='young', size='small', gender='female', coat='short')
    pets = pd.read_json("../petsite/static/js/pet_results.geojson")

    check_test = (pets['features'][0]['properties']['name'] == "Alvin" and
                  pets['features'][1]['properties']['name'] == "Bayla" and
                  pets['features'][2]['properties']['name'] == "Shoeshine" and
                  pets['features'][3]['properties']['name'] == "Odie")

    return check_test

if test_geojson():
    print("conversion test passed!")
else:
    print("conversion test failed!")
