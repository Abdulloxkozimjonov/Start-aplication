from django.db import models
from main.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    img = models.ImageField(upload_to='user_image/', null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam', null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Address(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Add(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    img = models.ImageField(upload_to='ad_img/')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    view = models.IntegerField(default=0)
    slugify = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name