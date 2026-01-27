from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def product_detail_view(*args, **kwargs):
    return HttpResponse("<h1>Product Detail View</h1>")