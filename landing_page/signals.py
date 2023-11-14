from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ProductTransfers



@receiver(post_save, sender=ProductTransfers)
def update_product_location(sender, instance, **kwargs):
    product = instance.product
    product.location = instance.destination_location
    product.save()