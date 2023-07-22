from django.db import models
from django.utils import timezone
from Account.models import User
# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=128,blank=False)
    company_manager = models.OneToOneField(User, related_name="company_manager", on_delete=models.CASCADE)
    company_email = models.EmailField(max_length=128)
    stripe_product_id = models.CharField(max_length=128,blank=True,null=True)
    premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now,editable=False)
    updated_at = models.DateTimeField(auto_now=True) 

    @property
    def manager_first_name(self):
        return self._manager_first_name
    
    @property
    def manager_last_name(self):
        return self._manager_last_name
    
    @property
    def manager_email(self):
        return self._manager_email
    
    @property
    def manager_password(self):
        return self._manager_password               

    def __str__(self):
        return f"{self.company_name}"
