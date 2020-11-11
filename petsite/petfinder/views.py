from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import pathlib
from petfinder_api.query import get_animal_breeds, authenticate, key, secret_key
import numpy as np

pf = authenticate(key, secret_key)

# Create your views here.
def make_dictionary(request):
    query = {k: v for k,v in request.GET.lists()}
    return query

# Writes a dictionary to a json file with a name specified in filename
def write_dictionary(query, filename):
    parent_dir = pathlib.Path(__file__).parent.parent.parent.absolute()
    filepath = parent_dir / 'tests' / filename
    with open(filepath, 'w') as fp:
        json.dump(query, fp)

# Determines if a breed exists for a given pet
def validate_breed(pet_type, breed_name):
    pet_breeds = np.char.lower(get_animal_breeds(pf, pet_type).astype('str'))
    return breed_name.lower() in pet_breeds

# This function performs all the necessary operations and checks to output the correct query to render
def prepare_query(request, pet_type):
    query = make_dictionary(request)
    write_dictionary(query, 'search.json')
    breed_error = False
    if 'breed' in query and query['breed'][0] != '':
        breed_error = not validate_breed(pet_type, query['breed'][0])
    if breed_error:
        query['breed'] = 'NOT FOUND'
    write_dictionary(query, 'test_breed_search.json')
    return query


def index(request):
    query = make_dictionary(request)
    # Form requests as a dictionary
    return render(request, 'petfinder/HomePage.html')
    
def dogs_request(request):
    query = prepare_query(request, 'dog')
    template = loader.get_template('petfinder/Petfinder_style.html')
    return HttpResponse(template.render({"search_query": query}, request))

def cats_request(request):
    query = make_dictionary(request)
    return render(request, 'petfinder/Cats.html')
def birds_request(request):
    query = make_dictionary(request)
    return render(request, 'petfinder/Birds.html')
def rabbits_request(request):
    query = make_dictionary(request)
    return render(request, 'petfinder/Rabbits.html')
def scales_request(request):
    query = make_dictionary(request)
    return render(request, 'petfinder/Scales.html')
