from .models import Product
from django import forms


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                "barcode_id",
                "product_name",
                "units",
                "cost_per_unit",
                "stock_value",
                "currency",
                "category",
                "description",
                "nature",
                "product_image"
                  ]