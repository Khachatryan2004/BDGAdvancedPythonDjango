from django.db import models


class Category(models.Model):
    categories = models.CharField('Categories', max_length=20)


class News(models.Model):
    news = models.ForeignKey(Category,
                             on_delete=models.CASCADE, verbose_name='Main Category')
    additional_category = models.ManyToManyField(Category,
                                                 blank=True, verbose_name='Additional Categories')
