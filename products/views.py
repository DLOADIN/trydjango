from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

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
        "my_fav_food": "Biriyani",
        "my_list": [425, 'Galvarino', 3123, 3484, 25, 'DTX' , 312],
    }
    return render(request, "AboutPage.html", my_context)


def new_product_detail_view(request):
    Newobject = Products.objects.get(id=1)
    context = {
        "title": Newobject.title,
        'summary': Newobject.summary
    }
    return render(request, "products/new_product_detail.html",context)

