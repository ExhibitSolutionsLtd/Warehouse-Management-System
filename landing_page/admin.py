from django.contrib import admin
from .models import Product, Order, Customer, Supplier, Location

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Location)