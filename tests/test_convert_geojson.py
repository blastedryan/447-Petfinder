from query import find_pets, authenticate, key, secret_key
from convert_to_geojson import write_file
import pytest
import json
import pandas as pd


pf = authenticate(key, secret_key)

def test_geojson_1():

    pets, _ = find_pets(pf, location='Baltimore, MD', animal_type='dog', breed='beagle',distance=100,age='young', size='small', coat='short')

    write_file(pets)
    
    pets = pd.read_json("../petsite/static/js/pet_results.geojson")


    check_test = (pets['features'][0]['properties']['name'] == "Alvin" and
                  pets['features'][1]['properties']['name'] == "Bayla" and
                  pets['features'][2]['properties']['name'] == "Shoeshine" and
                  pets['features'][3]['properties']['name'] == "Odie")

    return check_test

def test_geojson_2():

        pets, _ = find_pets(pf,location='Baltimore, MD', breed="Maine Coon", animal_type='cat', size="small",distance=50, coat='long')

        write_file(pets)
        
        pets = pd.read_json("../petsite/static/js/pet_results.geojson")

        check_test = (pets['features'][0]['properties']['name'] == "Mowgli" and
                      pets['features'][1]['properties']['name'] == "Mr. Peaches (Declawed)")

        return check_test
        
num_tests = 2
tests_passed = 0


if test_geojson_1():
    tests_passed += 1
if test_geojson_2():
    tests_passed += 1


if tests_passed == num_tests:
    print("All tests passed!")
else:
    print(tests_passed,"/",num_tests,"tests passed")
