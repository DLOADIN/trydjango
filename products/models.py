from django.db import models
from django.urls import reverse

# Create your models here.
# we can have TextField for large text inputs, 
# DecimalField for precise decimal numbers like prices
# CharField for short text inputs
# IntegerField for whole numbers
# BooleanField for true/false values
# DateTimeField for date and time values
# ForeignKey for relationships between models
# ManyToManyField for many-to-many relationships
class Products(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2) 
    summary = models.TextField()
    objects = models.Manager()

    def get_absolute_url(self):
        return f"/products/{self.pk}/"
    