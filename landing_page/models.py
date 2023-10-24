from django.db import models
from django.contrib.auth.models import User

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
    barcode_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    units = models.CharField(unit_choices)
    cost_per_unit = models.IntegerField()
    description = models.TextField()
    nature = models.CharField(nature_choices)
    product_image = models.ImageField("product_images")
    user = models.ForeignKey(User, related_name="created_by", on_delete=models.CASCADE)