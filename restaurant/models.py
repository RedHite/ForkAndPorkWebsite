from django.db import models


SPICYPOWER = (
    (1, 'no spicy'),
    (2, 'some spicy'),
    (3, 'spicy'),
    (4, 'very spicy'),
    (5, 'ultra spicy'),
)

VEGEOPTION = (
    (1, 'with meat'),
    (2, 'vegetarian'),
    (3, 'vegan'),
)

class Allergene(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    price = models.DecimalField(null=True, max_digits=6, decimal_places=3)
    calories = models.IntegerField(null=True)
    spicy = models.IntegerField(choices=SPICYPOWER)
    meat = models.IntegerField(choices=VEGEOPTION)
    picture = models.ImageField(null=True, blank=True)
    allergenes = models.ManyToManyField(Allergene)

    def __str__(self):
        return self.name