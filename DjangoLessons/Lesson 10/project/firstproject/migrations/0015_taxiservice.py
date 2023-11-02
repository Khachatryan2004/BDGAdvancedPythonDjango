# Generated by Django 4.2.6 on 2023-10-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0014_flower'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxiService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Service Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('rating', models.PositiveSmallIntegerField(default=0, verbose_name='Rating')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('contact_number', models.CharField(max_length=20, verbose_name='Contact Number')),
            ],
            options={
                'verbose_name': 'Taxi Service',
                'verbose_name_plural': 'Taxi Services',
            },
        ),
    ]