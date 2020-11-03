from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import pathlib
# Create your views here.
def index(request):
    # Form requests as a dictionary

    parent_dir = pathlib.Path(__file__).parent.parent.parent.absolute()
    filepath = parent_dir / 'tests' / 'search.json'
    query = {k: v for k,v in request.GET.lists()}
    with open(filepath, 'w') as fp:
        json.dump(query, fp)

    template = loader.get_template('petfinder/HomePage.html')

    return HttpResponse(template.render({"search_query":query}, request))

def dogs_request(request):
    return render(request, 'petfinder/Petfinder_style.html')
def cats_request(request):
    return render(request, 'petfinder/Cats.html')
def birds_request(request):
    return render(request, 'petfinder/Birds.html')
def rabbits_request(request):
    return render(request, 'petfinder/Rabbits.html')
def scales_request(request):
    return render(request, 'petfinder/Scales.html')
