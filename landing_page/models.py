from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Product(models.Model):
    unit_choices = [
        ("milligrams", "milligrams"),
        ("grams", "grams"),
        ("Kilograms", "Kilograms"),
        ("millilitres", "millilitres"),
        ("Litres", "Litres"),
        ("metres", "mitres"),
        ("Units", "Units")
    ]
    nature_choices = [
        ("Purchase", "Purchase"),
        ("Return", "Return"),
        ("Transfer", "Transfer"),
        ("Reject", "Reject")
    ]
    category_choices = [
        ("Grocery", "Grocery"),
        ("Stationery", "Stationery"),
        ("Furniture", "Furniture"),
        ("Jewellery", "Jewellery"),
        ("Clothing", "Clothing"),
        ("Electronic", "Electronic")
    ]
    sku = models.CharField(verbose_name = "Stock Keeping Unit", max_length=50) #Stock Keeping Unit
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50, choices=category_choices)
    description = models.TextField()
    location = models.CharField(verbose_name ="Location (e.g., Aisle/Shelf/Bin)", max_length=100)
    product_image = models.ImageField("product_images")
    user = models.ForeignKey(User, related_name="created_by", on_delete=models.CASCADE)
    item_created_at = models.DateTimeField(auto_now_add=True)
    item_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item_name}'


    def save(self):
        super().save()

        img = Image.open(self.product_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.product_image.path)


class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ("Inbound", "Inbound"),
        ("Outbound", "Outbound")
    ]
    order_id = models.CharField(verbose_name='Order ID', max_length=50)
    order_created_at = models.DateTimeField(auto_now_add=True)
    order_updated_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Product, related_name= "ordered_item", on_delete=models.CASCADE)
    order_type = models.CharField(verbose_name='Order Type', choices=ORDER_TYPE_CHOICES)
    total_items = models.PositiveIntegerField(verbose_name='Total Items')
    status = models.CharField(verbose_name='Status', choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed')])
    notes = models.TextField(verbose_name='Notes', blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    associated_name = GenericForeignKey('content_type', 'object_id')

    def __str__(self) -> str:
        return f'Order no: {self.order_id}'


class Customer(models.Model):
    cust_f_name = models.CharField(verbose_name='First Name', max_length=100)
    cust_l_name = models.CharField(verbose_name='Last Name', max_length=100)
    orders = GenericRelation(Order)
    email = models.EmailField(verbose_name='Email Address', max_length=50)
    mobile_no = models.PositiveIntegerField(verbose_name='Mobile No. e.g., 254712345678', max_length=12, blank=True, null=True)
    address = models.TextField(verbose_name='Address', blank=True)
    notes = models.TextField(verbose_name='Notes', blank=True)

    def __str__(self) -> str:
        return f'{self.cust_f_name} {self.cust_l_name}'

class Supplier(models.Model):
    sup_f_name = models.CharField(verbose_name='First Name', max_length=100)
    sup_l_name = models.CharField(verbose_name='Last Name', max_length=100)
    orders = GenericRelation(Order)
    email = models.EmailField(verbose_name='Email Address', blank=True, max_length=50)
    mobile_no = models.PositiveIntegerField(verbose_name='Mobile No. e.g., 254712345678', max_length=12, blank=True)
    address = models.TextField(verbose_name='Address', blank=True)
    notes = models.TextField(verbose_name='Notes', blank=True)

    def __str__(self) -> str:
        return f'{self.sup_f_name} {self.sup_l_name}'