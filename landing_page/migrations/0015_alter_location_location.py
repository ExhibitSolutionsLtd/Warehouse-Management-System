# Generated by Django 4.2.6 on 2023-11-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0014_alter_location_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
