# Generated by Django 4.2.6 on 2023-10-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(blank=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='sup_l_name',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
    ]