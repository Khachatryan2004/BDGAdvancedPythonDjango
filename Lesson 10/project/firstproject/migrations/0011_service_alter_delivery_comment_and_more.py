# Generated by Django 4.2.6 on 2023-10-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0010_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AlterField(
            model_name='delivery',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='product',
            field=models.CharField(max_length=20),
        ),
    ]
