from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from Account.models import User
from .models import Employee

@receiver(pre_save, sender=Employee)
def create_user_for_employee(sender, instance, *args, **kwargs):
    if instance.id is None:
        first_name = instance._first_name
        last_name = instance._last_name
        email = instance._email
        password = instance._password

        user = User(username=email, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        print(user)
        instance.user = user