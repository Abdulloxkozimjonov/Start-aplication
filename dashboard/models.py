from django.db import models
from main.models import User
from django.template.defaultfilters import slugify


class Address(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Ad(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    img = models.ImageField(upload_to='ad_img/')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    view = models.IntegerField(default=0)
    slugify = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name