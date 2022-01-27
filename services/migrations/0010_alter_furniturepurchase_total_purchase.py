# Generated by Django 4.0 on 2022-01-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_furniturepurchase_total_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniturepurchase',
            name='total_purchase',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]