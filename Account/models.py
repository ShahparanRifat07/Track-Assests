from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Custom User Model
Made changes so that user can login with email instead of username
"""
class User(AbstractUser):
    email = models.EmailField(unique=True, blank= False,editable=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} -- {self.username}"
    

