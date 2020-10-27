from petfinder_api.query import find_pets, authenticate, key, secret_key
from geopy.geocoders import Nominatim
import numpy as np
from pandas import DataFrame

pf = authenticate(key, secret_key)

def test_geocode():
    locator = Nominatim(user_agent='myGeocoder')
    pets, _ = find_pets(pf, animal_type='dog', location='Baltimore, MD', distance=25)
    pets['contact.address.address'] = pets['contact.address.city'].fillna('') + ', ' + \
                                      pets['contact.address.state'].fillna('') + ', ' + \
                                      pets['contact.address.postcode'].fillna('')
    unique_addresses = pets['contact.address.address'].unique()
    location_list = np.array([locator.geocode(x) for x in unique_addresses], dtype=object)
    lat_long_tup = np.array(location_list[:, 1])
    for i in range(len(unique_addresses)):
        pets.loc[pets['contact.address.address'] == unique_addresses[i], ['contact.address.lat', 'contact.address.long']] = lat_long_tup[i][0], lat_long_tup[i][1]

    print(pets[['contact.address.address', 'contact.address.lat', 'contact.address.long']])

    assert isinstance(pets, DataFrame)
