# Generated by Django 4.2.6 on 2023-11-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0007_alter_order_order_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
