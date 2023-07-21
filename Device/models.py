from django.db import models
from Company.models import Company
from django.utils import timezone
# Create your models here.

CONDITION = (
    ("1", "Good"),
    ("2", "Average"),
    ("3", "Bad"),
)

class Device(models.Model):
    name = models.CharField(max_length=128,blank=False)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='device_company')
    available = models.BooleanField(default=True)
    condition = models.CharField(max_length = 1, choices = CONDITION, default="1")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.name}"