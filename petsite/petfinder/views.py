from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.
def index(request):
    # Form requests as a dictionary
    query = {k: v for k,v in request.GET.lists()}
    with open('search.json', 'w') as fp:
        json.dump(query, fp)
    template = loader.get_template('petfinder/Petfinder_style.html')

    return HttpResponse(template.render({"search_query":query}, request))
