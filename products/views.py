from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_detail_view(request,*args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Product Detail View</h1>")


def Contactview(request,*args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Contact Details</h1>")

def Aboutview(request,*args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>About Page Details</h1>")