# Generated by Django 3.1.13 on 2021-12-24 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FurnitureSales',
            new_name='FurnitureSale',
        ),
    ]