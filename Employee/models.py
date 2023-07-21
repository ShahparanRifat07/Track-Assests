from django.db import models
from django.utils import timezone
from Account.models import User
from Company.models import Company

class Employee(models.Model):
    user = models.OneToOneField(User, related_name="employee", on_delete=models.CASCADE)
    employee_company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="employee_company")
    is_stuff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True) 

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self._password
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"