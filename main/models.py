from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    img = models.ImageField(upload_to='profile_img', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable= 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'