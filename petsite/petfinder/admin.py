from django.contrib import admin

from .models import Animal, Search

# Register your models here.
admin.site.register(Animal)
admin.site.register(Search)