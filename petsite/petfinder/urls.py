from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^dogs_request/$', views.dogs_request, name='Petfinder_style'),
    url(r'^cats_request/$', views.cats_request, name = 'Cats'),
    url(r'^birds_request/$', views.birds_request, name='Birds'),
    url(r'^rabbits_request/$', views.rabbits_request, name = 'Rabbits'),
    url(r'^scales_request/$', views.scales_request, name='Scales'),
    url(r'^horse_request/$', views.horse_request, name='Horse'),
    url(r'^barn_request/$', views.barn_request, name='Barn'),
    url(r'^furry_request/$', views.furry_request, name='Furry')
]