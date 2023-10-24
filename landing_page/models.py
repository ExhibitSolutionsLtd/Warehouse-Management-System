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
        ("Ksh.", "Ksh"),
        ("$.", "$"),
        ("£", "£"),
        ("€", "€")
    ]
    barcode_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    units = models.CharField(max_length=50, choices=unit_choices)
    cost_per_unit = models.IntegerField()
    stock_value = models.IntegerField()
    currency = models.CharField(max_length=50, choices=currency_choices)
    description = models.TextField()
    nature = models.CharField(max_length=50, choices=nature_choices)
    product_image = models.ImageField("product_images")
    user = models.ForeignKey(User, related_name="created_by", on_delete=models.CASCADE)


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)