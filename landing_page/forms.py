from .models import Product
from django import forms


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["barcode_id", "product_name", "units", "cost_per_unit", "description", "nature", "product_image"]