from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import pathlib
from petfinder_api.query import find_pets, get_animal_breeds, authenticate, key, secret_key
from petfinder_api.convert_to_json import df_to_geojson
import numpy as np

pf = authenticate(key, secret_key)

def save_pet_results(pets):
    useful_cols = ["age", "gender", "size", "name", "breeds.primary", "primary_photo_cropped.small"]
    geojson_dict = df_to_geojson(pets, properties=useful_cols,lat="contact.address.lat",lon="contact.address.long")
    geojson_str = json.dumps(geojson_dict, indent=2)
    filename = pathlib.Path(__file__).parent.absolute() / "search_results"/ "pet_results.geojson"
    with open(filename, 'w') as output_file:
        output_file.write('{}'.format(geojson_str))

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

def open_pet_results():
    parent_dir = pathlib.Path(__file__).parent.absolute()
    filename = parent_dir / "search_results"/ "pet_results.geojson"
    with open(filename, 'r') as f:
        json_data = json.load(f)
        return json_data


def index(request):
    query = make_dictionary(request)
    # Form requests as a dictionary
    return render(request, 'petfinder/HomePage.html')
    
def dogs_request(request):
    query = prepare_query(request, 'dog')

    print('\n' * 4, query, '\n'*4)

    search_queries = {
        'male': 'gender',
        'female': 'gender',
        'small': 'size'
    }


    petfind_query = {'animal_type': 'dog'}

    for k in query:
        if k == 'location':
            petfind_query['location'] = None if query[k][0].strip() == '' else query[k][0]

        elif k == 'breed':
            petfind_query['breed'] = None if query[k][0].strip() == '' else query[k][0]

        elif k in search_queries:
            petfind_query[search_queries[k]] = k

    

    json_data = {}
    if len(query) > 0:
    
        pets, _ = find_pets(pf, **petfind_query)

        save_pet_results(pets)
        json_data = open_pet_results()

    template = loader.get_template('petfinder/Petfinder_style.html')
    return HttpResponse(template.render({"search_query": query, 'the_json':json_data}, request))

def cats_request(request):
    json_data = open_pet_results()
    '''
    query = make_dictionary(request)
    return render(request, 'petfinder/Cats.html')
    
    return render(request, 'petfinder/Cats.html', {'the_json':json_data})
    '''


    query = make_dictionary(request)
    template = loader.get_template('petfinder/Cats.html')
    return HttpResponse(template.render({"search_query":query, 'the_json':json_data}, request))


def birds_request(request):
    query = make_dictionary(request)
    json_data = open_pet_results()
    return render(request, 'petfinder/Birds.html',  {'the_json':json_data})
def rabbits_request(request):
    query = make_dictionary(request)
    json_data = open_pet_results()
    return render(request, 'petfinder/Rabbits.html',  {'the_json':json_data})
def scales_request(request):
    query = make_dictionary(request)
    json_data = open_pet_results()
    return render(request, 'petfinder/Scales.html',  {'the_json':json_data})

