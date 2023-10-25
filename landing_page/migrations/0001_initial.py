# Generated by Django 4.2.6 on 2023-10-24 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('units', models.CharField(choices=[('milligrams', 'milligrams'), ('grams', 'grams'), ('Kilograms', 'Kilograms'), ('millilitres', 'millilitres'), ('Litres', 'Litres'), ('metres', 'mitres'), ('Units', 'Units')], max_length=50)),
                ('cost_per_unit', models.IntegerField()),
                ('stock_value', models.IntegerField()),
                ('currency', models.CharField(choices=[('Ksh.', 'Ksh'), ('$.', '$'), ('£', '£'), ('€', '€')], max_length=50)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Stationery', 'Stationery'), ('Furniture', 'Furniture'), ('Jewellery', 'Jewellery'), ('Clothing', 'Clothing')], max_length=50)),
                ('description', models.TextField()),
                ('nature', models.CharField(choices=[('Purchase', 'Purchase'), ('Return', 'Return'), ('Transfer', 'Transfer'), ('Reject', 'Reject')], max_length=50)),
                ('product_image', models.ImageField(upload_to='', verbose_name='product_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
