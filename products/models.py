from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2) 
    summary = models.TextField()