"""
This is a cache database that holds all query results in the past 24 hours
This is basically my first time writing python code so don't expect anything out of it
"""
import os
import numpy as np
from django.core.cache import cache
from petsite.petfinder_api.query import find_pets, authenticate, key, secret_key
from petpy.api import Petfinder
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

num_results = 50  # number of results we want
os.environ['DJANGO_SETTINGS_MODULE'] = 'petsite.petsite.settings'
locator = Nominatim(user_agent='myGeocoder')


def find_pets_with_cache(pf: Petfinder, location=None, animal_type=None, breed=None, size=None, gender=None, age=None,
                         color=None,
                         coat=None, org_name=None, distance=None, name=None, good_with=[], house_trained=None,
                         special_needs=None,
                         sort=None):
    # if cache is empty fill with query
    if cache.get('default') is None:
        pets, _ = find_pets(pf, location, animal_type, breed, size, gender, age, color,
                            coat, org_name, distance, name, good_with, house_trained, special_needs, sort)
        # if 'primary_photo_cropped' in pets.columns:
        #    del pets['primary_photo_cropped']
        cache.set('default', pets)
    else:
        pets = cache.get('default')

        # search cache for characteristics
        if animal_type is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['animal_type'] == animal_type]
        if breed is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['breeds'] == breed]
        if size is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['size'] == size]
        if gender is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['gender'] == gender]
        if age is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['age'] == age]
        if color is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['colors'] == color]
        if coat is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['coat'] == coat]
        if name is not None and pets.shape[0] >= num_results:
            pets = pets.loc[pets['name'] == name]

        # location search
        if location is not None and pets.shape[0] >= num_results:
            curr_location = locator.geocode(location)
            curr_latlong = (curr_location.latitude, curr_location.longitude)
            # remove results with no latlong
            pets = pets.loc[(np.isnan(pets['contact.address.lat']) == False) &
                            (np.isnan(pets['contact.address.long']) == False)]
            #pets = pets.loc[((geodesic(curr_latlong, (pets['contact.address.lat'], pets['contact.address.long'])).miles) < distance)]
            pets['new'] = geodesic((pets['contact.address.lat'], pets['contact.address.long']),curr_latlong).miles

        # if there are not enough results in the cache, run query and cache results
        if pets.shape[0] < num_results:
            pets, _ = find_pets(pf, location, animal_type, breed, size, gender, age, color,
                                coat, org_name, distance, name, good_with, house_trained, special_needs, sort)
            temp = cache.get('default')
            # if 'primary_photo_cropped' in pets.columns:
            #    del pets['primary_photo_cropped']
            if 'primary_photo_cropped' in temp.columns:
                del temp['primary_photo_cropped']
            pets = pets.append(temp, ignore_index=True)
            pets = pets.drop_duplicates(subset=['animal_type', 'gender', 'age', 'coat', 'name'])
            cache.set('default', pets)
        else:
            # if more results than wanted, drop bottom values until there are proper number of results
            while pets.shape[0] > num_results:
                pets.drop(pets.index[num_results])
    return pets
