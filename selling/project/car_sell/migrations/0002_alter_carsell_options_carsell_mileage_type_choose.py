# Generated by Django 4.2.6 on 2023-10-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_sell', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carsell',
            options={'ordering': ['-title'], 'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AddField(
            model_name='carsell',
            name='mileage_type_choose',
            field=models.CharField(blank=True, choices=[('KM', 'KM'), ('ML', 'ML')], max_length=3, verbose_name='Mileage Measurement Types'),
        ),
    ]
