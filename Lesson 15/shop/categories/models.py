from django.db import models


class TimesStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, )
    upgraded_at = models.DateTimeField(auto_now_add=True, )
    status = models.BooleanField()

    class Meta:
        abstract = True


class Category(TimesStampModel):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(TimesStampModel):
    price = models.FloatField()
    name = models.CharField(unique=True, max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'
