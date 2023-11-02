from django.db import models


class Manufacture(models.Model):
    name = models.CharField(unique=True, max_length=30)
    address = models.CharField(unique=True, max_length=250)
    email = models.EmailField(unique=True, max_length=250)
    created_at = models.DateField()
    slug = models.SlugField(unique=True, max_length=30)

    def __str__(self):
        return f"{self.name}"

    class Mate:
        ordering = ["-name"]


class Car(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=30)
    created_at = models.DateField()
    slug = models.SlugField(unique=True, max_length=30)
    hp = models.PositiveIntegerField()
    tire = (
        ("A", "AWD"),
        ("F", "FWD"),
        ("R", "RWD"),
    )
    position = models.CharField(max_length=1, choices=tire)
    image = models.ImageField(upload_to="car/")
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.manufacture}, {self.name}"

    class Mate:
        ordering = ["-name"]

