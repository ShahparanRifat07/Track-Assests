from django.db import models
from Company.models import Company
from django.utils import timezone
from Employee.models import Employee
import uuid
# Create your models here.

CONDITION = (
    ("1", "Good"),
    ("2", "Average"),
    ("3", "Bad"),
)

class Device(models.Model):
    name = models.CharField(max_length=128,blank=False)
    product_id = models.CharField(max_length=6,blank=False,null=False)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='device_company')
    available = models.BooleanField(default=True)
    condition = models.CharField(max_length = 1, choices = CONDITION, default="1")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        random_uuid = uuid.uuid4()
        self.product_id = str(random_uuid)[:6]
        super(Device, self).save(*args, **kwargs)
    
    

class DeviceLog(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE,related_name='device_log')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='employee_log')
    checkout_date = models.DateField()
    checkin_date = models.DateField(null=True,blank=True)
    condition_at_checkout_day = models.CharField(max_length = 1, choices = CONDITION)
    condition_at_checkin_day = models.CharField(max_length = 1, choices = CONDITION,null=True,blank=True)
    comment = models.TextField(max_length=512)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.device.name}---{self.employee.user.last_name}"
