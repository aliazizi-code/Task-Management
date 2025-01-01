from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=12,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,12}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
        ],
    )
    username = models.CharField(unique=False, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.phone_number
