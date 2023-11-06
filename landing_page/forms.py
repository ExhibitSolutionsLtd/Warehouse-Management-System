from .models import Product, Order, Customer, Supplier
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
        
class OrderCreationForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=False)

    class Meta:
        model = Order
        exclude = ['associated_name', 'content_type', 'object_id']

    def __init__(self, *args, **kwargs):
          super(OrderCreationForm, self).__init__(*args, **kwargs)
          
          if self.instance.id:  # If order already exists
              if self.instance.order_type == "Inbound":
                  self.fields['supplier'].initial = self.instance.associated_name
              else:
                  self.fields['customer'].initial = self.instance.associated_name

    def save(self, commit=True):
        instance = super(OrderCreationForm, self).save(commit=False)
        
        if instance.order_type == "Inbound":
            instance.associated_name = self.cleaned_data['supplier']
        else:
            instance.associated_name = self.cleaned_data['customer']

        if commit:
            instance.save()
        return instance
    
class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['cust_f_name', 'cust_l_name', 'email', 'mobile_no', 'address', 'notes']


class SupplierCreationForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['sup_f_name', 'sup_l_name', 'email', 'mobile_no', 'address', 'notes']