from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    this class created for adding the table in database
    """
    age = models.IntegerField(verbose_name="Age")
    is_verified = models.IntegerField()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
