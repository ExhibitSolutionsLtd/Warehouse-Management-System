# Generated by Django 4.2.6 on 2023-11-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
