# Generated by Django 4.2.6 on 2023-10-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='country',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Which country produces'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]