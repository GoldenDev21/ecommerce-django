from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mailing_list = models.BooleanField(null=True)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_staff:
        instance.profile.save(user=instance)


class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        (1, 'Shipping'),
        (2, 'Billing')
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='addresses')
    primary = models.BooleanField()
    type = models.IntegerField(choices=ADDRESS_TYPE_CHOICES)
    line_1 = models.CharField(max_length=120)
    line_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=3)
    zip = models.CharField(max_length=15)
