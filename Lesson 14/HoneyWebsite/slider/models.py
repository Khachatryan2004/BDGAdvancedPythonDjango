from django.db import models


class Slider(models.Model):
    title1 = models.CharField(max_length=40)
    title2 = models.CharField(max_length=40)
    description = models.TextField()
    image1 = models.ImageField(upload_to='slider/')
    image2 = models.ImageField(upload_to='slider/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title1}'
