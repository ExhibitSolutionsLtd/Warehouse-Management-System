# Generated by Django 4.2.6 on 2023-11-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0010_location_alter_order_order_type_transfers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfers',
            old_name='trans_to',
            new_name='transfer_to',
        ),
    ]
