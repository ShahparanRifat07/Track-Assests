from django.db import models
from django.utils import timezone
from Account.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=128,blank=False)
    company_admin = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}--{self.company_admin.username}"
