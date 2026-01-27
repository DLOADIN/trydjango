from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_detail_view(request,*args, **kwargs):
    return render(request, "index.html",{})

def Contactview(request,*args, **kwargs):
    print(args, kwargs)
    return render(request, "Contactpage.html",{})

def Aboutview(request,*args, **kwargs):
    print(args, kwargs)
    my_context = {
        "my_name": "DTX Team",
        "my_age": "24",
        "my_hobby": "Coding",
        "my_fav_food": "Biriyani"
    }
    return render(request, "AboutPage.html", my_context)