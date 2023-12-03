from django.db import models


class ForAPI(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
