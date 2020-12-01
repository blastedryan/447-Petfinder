from django.contrib import admin

from .models import Animal, Search, Card, CardItem

# Register your models here.
admin.site.register(Animal)
admin.site.register(Search)
admin.site.register(Card)
admin.site.register(CardItem)