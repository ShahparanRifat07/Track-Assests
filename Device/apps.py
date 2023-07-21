from django.apps import AppConfig


class DeviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Device'

    def ready(self):
        import Device.signals
