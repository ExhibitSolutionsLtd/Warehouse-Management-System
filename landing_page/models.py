from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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
    sku = models.CharField(verbose_name = "SKU", max_length=50) #Stock Keeping Unit
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50, choices=category_choices)
    description = models.TextField()
    # nature = models.CharField(max_length=50, choices=nature_choices)
    location = models.CharField(verbose_name ="Location (e.g., Aisle/Shelf/Bin)", max_length=100)
    product_image = models.ImageField("product_images")
    user = models.ForeignKey(User, related_name="created_by", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_name}'


    def save(self):
        super().save()

        img = Image.open(self.product_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.product_image.path)


class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ("inbound", "Inbound"),
        ("Outbound", "Outbound")
    ]
    order_id = models.CharField(verbose_name='Order ID', max_length=50)
    order_date = models.DateField(verbose_name='Order Date')
    order_type = models.CharField(verbose_name='Order Type', choices=ORDER_TYPE_CHOICES)
    associated_name = models.CharField(verbose_name='Supplier/Customer Name', max_length=100)
    total_items = models.IntegerField(verbose_name='Total Items')
    status = models.CharField(verbose_name='Status', choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed')])
    notes = models.TextField(verbose_name='Notes', blank=True)