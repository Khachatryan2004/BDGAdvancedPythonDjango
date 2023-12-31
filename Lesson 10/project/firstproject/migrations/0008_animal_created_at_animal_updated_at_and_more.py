# Generated by Django 4.2.6 on 2023-10-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0007_alter_animal_options_animal_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
