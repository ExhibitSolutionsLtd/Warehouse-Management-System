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

    currency_choices = [
        ("Ksh", "Ksh"),
        ("$", "$"),
        ("£", "£"),
        ("€", "€")
    ]
    category_choices = [
        ("Food", "Food"),
        ("Stationery", "Stationery"),
        ("Furniture", "Furniture"),
        ("Jewellery", "Jewellery"),
        ("Clothing", "Clothing")
    ]
    sku = models.CharField(verbose_name = "SKU", max_length=50) #Stock Keeping Unit
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50, choices=category_choices)
    description = models.TextField()
    # nature = models.CharField(max_length=50, choices=nature_choices)
    location = models.CharField(verbose_name="Location (e.g., Aisle/Shelf/Bin)", max_length=100)
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