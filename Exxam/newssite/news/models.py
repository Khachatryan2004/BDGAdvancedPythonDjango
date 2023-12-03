from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class News(TimestampedModel):
    news = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Categories")
    additional_category = models.ManyToManyField(Category, blank=True, null=True, related_name="additional_categories")
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.news}"

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

