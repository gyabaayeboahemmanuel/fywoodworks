# Generated by Django 4.0 on 2022-01-28 01:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_woodfrombush_sell_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnituresupply',
            name='date_recorded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wooditemsale',
            name='date_sold',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machinework',
            name='machine_work_type',
            field=models.CharField(choices=[('Planing', 'Planing'), ('Saw', 'Saw'), ('Ripping 1X12 Board', 'Ripping 1X12 Boards'), ('2X6 & 2X8 wood', '2X6 & 2X8 wood'), ('Beam 3X12', 'Beam 3X12'), ('Beam 4X12', 'Beam 4X12'), ('Wabire & Asemfra', 'Wabire & Asemfra'), ('Bed Machine', 'Bed Machine'), ('Door', 'Door'), ('Door Gate', 'Door Gate'), ('Ban-Saw', 'Ban-Saw'), ('Mono Desk', 'Mono Desk'), ('Door and Cramping', 'Door and Cramping'), ('Frame Plaining 3 in 1', 'Frame Plaining 3 in 1'), ('2 in 1 & Door Frame', '2 in 1 & Door Frame')], max_length=30),
        ),
        migrations.AlterField(
            model_name='woodfrombush',
            name='description',
            field=models.CharField(choices=[('2 X 8 - Red Wood', '2 X 8 - Red Wood'), ('2 X 8 - Ky3nky3n', '2 X 8 - Ky3nky3n'), ('2 X 8 - Oframe', '2 X 8 - Oframe'), ('2 X 8 - Odum', '2 X 8 - Odum'), ('2 X 8 - Saiba', '2 X 8 - Saiba'), ('2 X 8 - Wawa', '2 X 8- Wawa'), ('2 X 6 - Red Wood', '2 X 6 - Red Wood'), ('2 X 6 - Ky3nky3n', '2 X 6 - Ky3nky3n'), ('2 X 6 - Oframe', '2 X 6 - Oframe'), ('2 X 6 - Odum', '2 X 6 - Odum'), ('2 X 6 - Saiba', '2 X 6 - Saiba'), ('2 X 6 - Wawa', '2 X 6- Wawa'), ('1 X 9 - Ky3nky3n', '1 X 9 - Ky3nky3n'), ('1 X 9 - Red Wood', '1 X 9 - Red Wood'), ('1 X 9 - Oframe', '1 X 9 - Oframe'), ('1 X 9 - Odum', '1 X 9 - Odum'), ('1 X 9 - Saiba', '1 X 9 - Saiba'), ('1 X 9 - Wawa', '1 X 9- Wawa'), ('1 X 10 - Ky3nky3n', '1 X 10 - Ky3nky3n'), ('1 X 10 - Red Wood', '1 X 10 - Red Wood'), ('1 X 10 - Oframe', '1 X 10 - Oframe'), ('1 X 10 - Odum', '1 X 10 - Odum'), ('1 X 10 - Saiba', '1 X 10 - Saiba'), ('1 X 10 - Wawa', '1 X 10- Wawa'), ('1 X 12 - Ky3nky3n', '1 X 12 - Ky3nky3n'), ('1 X 12 - Red Wood', '1 X 12 - Red Wood'), ('1 X 12 - Oframe', '1 X 12 - Oframe'), ('1 X 12 - Odum', '1 X 12 - Odum'), ('1 X 12 - Saiba', '1 X 12 - Saiba'), ('1 X 12 - Wawa', '1 X 12- Wawa'), ('Ceiling Buttons', 'Ceiling Buttons')], max_length=30),
        ),
    ]
