from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import pathlib
# Create your views here.
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
    query = make_dictionary(request)
    template = loader.get_template('petfinder/Petfinder_style.html')
    return HttpResponse(template.render({"search_query":query}, request))

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
