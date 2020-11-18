from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import pathlib
import os


# Create your views here.

def open_pet_results():
    parent_dir = pathlib.Path(__file__).parent.absolute()
    filename = parent_dir / "search_results"/ "pet_results.geojson"
    with open(filename, 'r') as f:
        json_data = json.load(f)
        return json_data

def make_dictionary(request):
    parent_dir = pathlib.Path(__file__).parent.parent.parent.absolute()
    filepath = parent_dir / 'tests' / 'search.json'
    query = {k: v for k,v in request.GET.lists()}
    with open(filepath, 'w') as fp:
        json.dump(query, fp)

    return query


def index(request):
    query = make_dictionary(request)
    # Form requests as a dictionary
    return render(request, 'petfinder/HomePage.html')
    
def dogs_request(request):

    json_data = open_pet_results()
    
    
    query = make_dictionary(request)
    template = loader.get_template('petfinder/Petfinder_style.html')
    return HttpResponse(template.render({"search_query":query, 'the_json':json_data}, request))
    

    #return render(request, 'petfinder/Petfinder_style.html', {'the_json':json_data})
    
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

    json_data = open_pet_results()
    
    
    query = make_dictionary(request)
    template = loader.get_template('petfinder/Birds.html')
    return HttpResponse(template.render({"search_query":query, 'the_json':json_data}, request))


def rabbits_request(request):

    json_data = open_pet_results()
    
    
    query = make_dictionary(request)
    template = loader.get_template('petfinder/Rabbits.html')
    return HttpResponse(template.render({"search_query":query, 'the_json':json_data}, request))

    
def scales_request(request):

    json_data = open_pet_results()
    
    
    query = make_dictionary(request)
    template = loader.get_template('petfinder/Scales.html')
    return HttpResponse(template.render({"search_query":query, 'the_json':json_data}, request))


