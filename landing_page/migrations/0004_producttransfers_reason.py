# Generated by Django 4.2.6 on 2023-12-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0003_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransfers',
            name='reason',
            field=models.TextField(default='Hello'),
        ),
    ]
