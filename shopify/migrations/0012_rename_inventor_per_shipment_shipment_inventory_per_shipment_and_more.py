# Generated by Django 4.0.5 on 2022-06-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0011_alter_shipmentcontainer_added_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='inventor_per_shipment',
            new_name='inventory_per_shipment',
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='log_type',
            field=models.CharField(choices=[('INVENTORY_TYPE', 'Inventory Type'), ('INVENTORY', 'Inventory'), ('SHIPMENT', 'Shipment')], default='INVENTORY', max_length=25),
        ),
    ]
