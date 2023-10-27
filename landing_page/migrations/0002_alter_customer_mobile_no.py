# Generated by Django 4.2.6 on 2023-10-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_no',
            field=models.PositiveIntegerField(blank=True, max_length=12, null=True, verbose_name='Mobile No. e.g., 254712345678'),
        ),
    ]
