from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Device,DeviceLog

@receiver(post_save, sender=DeviceLog)
def update_(sender, instance,created, *args, **kwargs):
    if created:
        Device.objects.filter(id = instance.device.id).update(available=False)