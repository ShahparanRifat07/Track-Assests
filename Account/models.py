from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Custom User Model
"""
class User(AbstractUser):
    email = models.EmailField(unique=True, blank= False)
    REQUIRED_FIELDS = ["email"]
    def __str__(self):
        return self.username
