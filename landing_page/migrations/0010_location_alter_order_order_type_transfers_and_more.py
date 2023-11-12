# Generated by Django 4.2.6 on 2023-11-12 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0009_alter_order_object_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(blank=True, choices=[('Inbound', 'Inbound'), ('Outbound', 'Outbound')], verbose_name='Order Type'),
        ),
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.product')),
                ('trans_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.location')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.location', verbose_name='Location (e.g., Aisle/Shelf/Bin)'),
        ),
    ]
