# Generated by Django 4.2.6 on 2023-10-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0015_taxiservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Movie Title')),
                ('director', models.CharField(max_length=50, verbose_name='Director')),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('genre', models.CharField(max_length=30, verbose_name='Genre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('rating', models.PositiveSmallIntegerField(default=0, verbose_name='Rating')),
                ('duration', models.PositiveIntegerField(verbose_name='Duration (minutes)')),
                ('language', models.CharField(max_length=20, verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]