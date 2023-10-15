from django.db import models


class Car(models.Model):
    brand = models.CharField('Brand', max_length=30, unique=False)
    hp = models.PositiveIntegerField('HorsePower')
    color = models.CharField('Color', max_length=20)
    country = models.CharField('Which country produces', max_length=40, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.id} -> {self.brand}"

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Person(models.Model):
    gender = models.CharField('Gender: MALE or FEMALE', max_length=10)
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    profession = models.CharField('Profession', max_length=30, blank=True, null=True)
    age = models.PositiveSmallIntegerField('Age')
    birth_date = models.DateField('Birth Date')
    created_at = models.DateTimeField('Created At', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class Animal(models.Model):
    gender = models.CharField('Gender of animal', max_length=10)
    animal_owner_name = models.CharField(max_length=20, blank=True, null=True)
    animal_owner_number = models.PositiveIntegerField('Number')
    city = models.CharField('City', max_length=30)
    breed = models.CharField(max_length=15)
    age_animal = models.PositiveSmallIntegerField('Age')
    color = models.CharField('Color', max_length=20)
    description = models.TextField('Problem of animal', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.color} {self.breed}"

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'


class Delivery(models.Model):
    nickname = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    rating = models.PositiveSmallIntegerField('Rate us from 1 to 10')
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nickname} {self.rating} {self.product}"

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Delivery'


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Review(models.Model):
    reviewer = models.CharField('Name', max_length=15)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.reviewer}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Flower(models.Model):
    name = models.CharField('Flower Name', max_length=30)
    petal_color = models.CharField('Petal Color', max_length=30)
    stem_color = models.CharField('Stem Color', max_length=30)
    season = models.CharField('Bloom Season', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Flower'
        verbose_name_plural = 'Flowers'


class TaxiService(models.Model):
    name = models.CharField('Service Name', max_length=50)
    description = models.TextField('Description', blank=True, null=True)
    rating = models.PositiveSmallIntegerField('Rating', default=0)
    city = models.CharField('City', max_length=30)
    contact_number = models.CharField('Contact Number', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Taxi Service'
        verbose_name_plural = 'Taxi Services'


class Movie(models.Model):
    title = models.CharField('Movie Title', max_length=100)
    director = models.CharField('Director', max_length=50)
    release_date = models.DateField('Release Date')
    genre = models.CharField('Genre', max_length=30)
    description = models.TextField('Description', blank=True, null=True)
    rating = models.PositiveSmallIntegerField('Rating', default=0)
    duration = models.PositiveIntegerField('Duration (minutes)')
    language = models.CharField('Language', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
