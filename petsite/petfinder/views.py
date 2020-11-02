from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):

    template = loader.get_template('petfinder/Homepage.html')
    return HttpResponse(template.render({}, request))
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