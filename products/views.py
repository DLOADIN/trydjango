from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from .forms import ProductForm, RawProductForm

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



def product_create_newproduct(request):
     # Initialize the form with POST data if available
    form = ProductForm(request.POST or None)

    # If the form is valid, save the new product
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }
    # Pass the form to the template context
    return render(request, "products/product_create.html", context)


def product_create_rawform(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Products.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)
