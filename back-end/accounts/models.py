from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_on_mailing_list = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        (1, 'Shipping'),
        (2, 'Billing')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses')
    primary = models.BooleanField()
    type = models.IntegerField(choices=ADDRESS_TYPE_CHOICES)
    line_1 = models.CharField(max_length=120)
    line_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=3)
    zip = models.CharField(max_length=15)
