# Generated by Django 3.1.13 on 2021-12-23 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('unit_expenses_on_work', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.IntegerField()),
                ('date_made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralExpence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_type', models.CharField(choices=[('2 X 4', '2 X 4'), ('2 X 6', '2 X 6'), ('2 X 8', '2 X 8'), ('2 X 2', '2 X 2'), ('1 X 9', '1 X 9'), ('1 X 10', '1 X 10'), ('1 X 12', '1 X 12'), ('Wawa Board', 'Wawa Board'), ('Nyamedua', 'Nyamedua'), ('Saba', 'Saba'), ('Ceiling Buttons', 'Ceiling Buttons')], max_length=30)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='MachineWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_work_type', models.CharField(choices=[('Planning', 'Planning'), ('Saw', 'Saw'), ('Ripping', 'Ripping')], max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WoodSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('date_sold', models.DateTimeField(auto_now_add=True)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.log')),
            ],
        ),
        migrations.CreateModel(
            name='WoodFromBush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woodtype', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('processed', models.BooleanField(default=False)),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.operator')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField()),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.staff')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='wood_from_bush',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.woodfrombush'),
        ),
        migrations.CreateModel(
            name='FurnitureSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_sold', models.DateTimeField(auto_now_add=True)),
                ('furnitureInventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.furnitureinventory')),
            ],
        ),
    ]