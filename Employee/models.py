from django.db import models
from django.utils import timezone
from Account.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_company = models.ForeignKey(to="Company.Company",on_delete=models.CASCADE,related_name="employee_company")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now) 

    @property
    def first_name(self):
        return self.first_name
    
    @property
    def last_name(self):
        return self.last_name
    
    @property
    def email(self):
        return self.email
    
    @property
    def password(self):
        return self.password
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"