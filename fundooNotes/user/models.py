from django.db import models


class User(models.Model):
    """
    created this class for table in database
    """
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)