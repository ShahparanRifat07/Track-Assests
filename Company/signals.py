from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from Employee.models import Employee
from Account.models import User
from .models import Company


@receiver(pre_save, sender=Company)
def create_employee_manager_for_company(sender, instance, *args, **kwargs):
    if instance.id is None:
        #creating admin for institution
        first_name = instance._manager_first_name
        last_name = instance._manager_last_name
        email = instance._manager_email
        password = instance._manager_password

        user = User(username=email, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        
        instance.company_manager = user