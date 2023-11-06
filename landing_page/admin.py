from django.contrib import admin
from .models import Product, Customer, Supplier, InboundOrder, OutboundOrder

# Register your models here.

admin.site.register(Product)
admin.site.register(InboundOrder)
admin.site.register(OutboundOrder)
admin.site.register(Customer)
admin.site.register(Supplier)