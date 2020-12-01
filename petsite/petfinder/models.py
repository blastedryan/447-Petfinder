from django.db import models

# Create your models here.
class Search(models.Model):
    location = models.CharField(max_length=200)
    animal_type = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    color = models.CharField(max_length=200)
    coat = models.CharField(max_length=200)
    org_name = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    good_with_dogs = models.BooleanField()
    good_with_children = models.BooleanField()
    sort = models.CharField(max_length=200)

class Animal(models.Model):
    location = models.CharField(max_length=200)
    animal_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    color = models.CharField(max_length=200)
    coat = models.CharField(max_length=200)
    org_id = models.CharField(max_length=200)
    org_name = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)
    good_with_dogs = models.BooleanField()
    good_with_children = models.BooleanField()
    house_trained = models.BooleanField()
    special_needs = models.BooleanField()
    sort = models.CharField(max_length=200)


class Card(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class CardItem(models.Model):
    FORMS = (
        ('checkbox', 'checkbox'),
        ('text', 'text')
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, default=None)
    form = models.CharField(max_length=200, choices=FORMS, default=None)
    image = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.name