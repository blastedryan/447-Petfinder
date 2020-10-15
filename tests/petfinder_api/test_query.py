from petfinder_api.query import find_pets, authenticate, key, secret_key
from pandas import DataFrame
from petpy.exceptions import PetfinderInvalidCredentials

pf = authenticate(key, secret_key)
NUM_TESTS = 5
MAX_PETS = 100

def test_authenticate_success(key_val, secret_val):
    try:
        authenticate(key_val, secret_val)
        print("Authentication success test PASSED")
        return 1
    except PetfinderInvalidCredentials as err:
        print("Authentication success test FAILED")
        return 0

def test_authenticate_fail(key_val, secret_val):
    try:
        authenticate(key_val, secret_val)
        print("Authentication fail test FAILED")
        return 0
    except PetfinderInvalidCredentials as err:
        print("Authentication fail test PASSED")
        return 1

def test_petfind():
    pets = find_pets(pf)

    if isinstance(pets, DataFrame) and pets.shape[0] == MAX_PETS:
        print('Pet Finder General Search PASSED')
        return 1
    else:
        print('Pet Finder General Search FAILED')
        return 0

def test_petfind_complex():
    pets = find_pets(pf, location='Baltimore, MD', animal_type='dog', breed='beagle', distance=50, name='Bayla',
                     age='young', size='small', gender='female', coat='short')
    if isinstance(pets, DataFrame) and pets['name'][0] == 'Bayla':
        print('Pet Finder Complex Search PASSED')
        return 1
    else:
        print('Pet Finder Complex Search FAILED')
        return 0

def test_petfind_goodwith():
    pets = find_pets(pf, good_with=['cat', 'dog'])

    if all(pets['environment.cats']) and all(pets['environment.dogs']):
        print('Pet Finder Good With PASSED')
        return 1
    else:
        print('Pet Finder Good With FAILED')
        return 0



if __name__ == '__main__':
    num_tests_passed = 0
    num_tests_passed += test_authenticate_success(key, secret_key)
    num_tests_passed += test_authenticate_fail('hello', 'hello')
    num_tests_passed += test_petfind()
    num_tests_passed += test_petfind_complex()
    num_tests_passed += test_petfind_goodwith()

    print('TESTS PASSED: ' + str(num_tests_passed) + '/' + str(NUM_TESTS))

