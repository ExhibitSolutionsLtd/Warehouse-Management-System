from django.contrib import admin
from .models import Product, Order, Customer, Supplier

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Supplier)