from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Custom User Model
"""
class User(AbstractUser):
    email = models.EmailField(unique=True, blank= False,editable=False)
    REQUIRED_FIELDS = ["email"]
    def __str__(self):
        return f"{self.first_name} {self.last_name} -- {self.username}"
