# Generated by Django 4.0 on 2022-01-20 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_alter_furniturepurchase_total_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='furnituresupply', to='services.furnitureinventory')),
            ],
        ),
    ]