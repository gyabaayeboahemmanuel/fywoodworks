# Generated by Django 4.0 on 2022-01-20 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_staff_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='other_names',
        ),
    ]