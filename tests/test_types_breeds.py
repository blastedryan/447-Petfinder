from petfinder_api.query import get_animal_breeds, get_animal_types, authenticate, key, secret_key
import pytest
import numpy as np

pf = authenticate(key, secret_key)

# Types of animals should be ['Dog' 'Cat' 'Rabbit' 'Small & Furry' 'Horse' 'Bird' 'Scales, Fins & Other' 'Barnyard']
def test_types():
    animal_types = get_animal_types(pf)
    animal_list = np.array(['Dog', 'Cat', 'Rabbit', 'Small & Furry', 'Horse', 'Bird', 'Scales, Fins & Other', 'Barnyard'])
    # print(animal_types)
    assert isinstance(animal_types, np.ndarray)
    assert np.array_equal(animal_types, animal_list)

# If you ever need an breed for a particular animal for testing, uncomment the print statement related to the animal
# and run the test
def test_breeds():
    cat_breeds = get_animal_breeds(pf, 'cat')
    # print(cat_breeds)
    assert isinstance(cat_breeds, np.ndarray)
    assert 'Toyger' in cat_breeds

    dog_breeds = get_animal_breeds(pf, 'dog')
    # print(dog_breeds)
    assert isinstance(dog_breeds, np.ndarray)
    assert 'American Bulldog' in dog_breeds

    rabbit_breeds = get_animal_breeds(pf, 'rabbit')
    # print(rabbit_breeds)
    assert isinstance(dog_breeds, np.ndarray)
    assert 'Rhinelander' in rabbit_breeds

    smallfurry_breeds = get_animal_breeds(pf, 'small-furry')
    # print(smallfurry_breeds)
    assert isinstance(smallfurry_breeds, np.ndarray)
    assert 'Rat' in smallfurry_breeds

    bird_breeds = get_animal_breeds(pf, 'bird')
    # print(bird_breeds)
    assert isinstance(bird_breeds, np.ndarray)
    assert 'Chicken' in bird_breeds

    horse_breeds = get_animal_breeds(pf, 'horse')
    # print(horse_breeds)
    assert isinstance(horse_breeds, np.ndarray)
    assert 'Arabian' in horse_breeds

    scalesfins_breeds = get_animal_breeds(pf, 'scales-fins-other')
    # print(scalesfins_breeds)
    assert isinstance(scalesfins_breeds, np.ndarray)
    assert 'Fire Salamander' in scalesfins_breeds

    barnyard_breeds = get_animal_breeds(pf, 'barnyard')
    # print(barnyard_breeds)
    assert isinstance(barnyard_breeds, np.ndarray)
    assert 'Goat' in barnyard_breeds