from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import pathlib

import petfinder_api.query as q

# Create your views here.

def make_dictionary(request):
    parent_dir = pathlib.Path(__file__).parent.parent.parent.absolute()
    filepath = parent_dir / 'tests' / 'search.json'
    query = {k: v for k,v in request.GET.lists()}
    with open(filepath, 'w') as fp:
        json.dump(query, fp)

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

    search_queries = {
        'gender': ['male', 'female'],
        'age': ['young', 'medium', 'old'],
        'hair_type': ['hairless', 'short_hair', 'mediumHair', 'longHair', 'wire', 'curly']
    }

    json_data = open_pet_results()
    
    query = make_dictionary(request)

    pf = q.authenticate(q.key, q.secret_key)

    petfind_query = {
        'location': 'Baltimore, MD',
        'breed': 'beagle',
        'animal_type': 'dog',
        'size': 'small',
        'distance': 100,
        'age': 'young',
        'coat': 'short'
    }

    pets, _ = q.find_pets(pf, **petfind_query)

    print(pets)


    template = loader.get_template('petfinder/Petfinder_style.html')
    #return render(request, 'petfinder/Petfinder_style.html', {'the_json':json_data})
    return HttpResponse(template.render({"search_query":query, 'the_json':json_data}, request))

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

