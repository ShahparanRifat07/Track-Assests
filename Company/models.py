from django.db import models
from django.utils import timezone
from Employee.models import Employee
# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=128,blank=False)
    company_manager = models.OneToOneField(Employee, on_delete=models.CASCADE)
    company_email = models.EmailField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now) 

    @property
    def manager_first_name(self):
        return self.manager_first_name
    
    @property
    def manager_last_name(self):
        return self.manager_last_name
    
    @property
    def manager_email(self):
        return self.manager_email
    
    @property
    def manager_password(self):
        return self.manager_password

    def __str__(self):
        return f"{self.name}"
