# Generated by Django 4.0.5 on 2022-06-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0013_alter_shipmentcontainer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentcontainer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
