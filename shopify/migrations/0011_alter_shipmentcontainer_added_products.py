# Generated by Django 4.0.5 on 2022-06-12 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0010_alter_shipmentcontainer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentcontainer',
            name='added_products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopify.inventory'),
        ),
    ]
