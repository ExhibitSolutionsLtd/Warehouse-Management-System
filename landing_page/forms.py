from .models import Product, InboundOrder, OutboundOrder, Customer, Supplier
from django import forms


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                "sku",
                "item_name",
                "quantity",
                "category",
                "location",
                "description",
                "product_image",
                  ]
        
class InboundOrderCreationForm(forms.ModelForm):
    class Meta:
        model = InboundOrder
        fields = [ "order_id", "associated_name", "item", "order_type", "total_items", "status", "notes"]

class OutboundOrderCreationForm(forms.ModelForm):
    class Meta:
        model = OutboundOrder
        fields = [ "order_id", "associated_name", "item", "order_type", "total_items", "status", "notes"]


class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['cust_f_name', 'cust_l_name', 'email', 'mobile_no', 'address', 'notes']


class SupplierCreationForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['sup_f_name', 'sup_l_name', 'email', 'mobile_no', 'address', 'notes']