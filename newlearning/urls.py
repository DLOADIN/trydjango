"""
URL configuration for newlearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import product_detail_view, Aboutview, Contactview   
from products.views import new_product_detail_view 
from products.views import product_create_newproduct, product_create_rawform                                              

urlpatterns = [
    path('products/', product_detail_view),
    path('About/', Aboutview),
    path('Contact/', Contactview),
    path('New Products/', new_product_detail_view),
    path('New Form Page/', product_create_newproduct),
    path('Raw Form Page/', product_create_rawform),
    path('admin/', admin.site.urls),
]
