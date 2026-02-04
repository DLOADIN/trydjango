from .models import Products
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price',
            'summary',
        ]
class RawProductForm(forms.Form):
    title = forms.CharField(label='Product Title', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(initial=199.99, max_digits=10, decimal_places=2)
    summary = forms.CharField(widget=forms.Textarea)

