from .models import Device,DeviceLog
from django.forms import ModelForm, TextInput

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ["name","condition","available"]
        required_fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Device Name'
                }),
        }

class DeviceLogForm(ModelForm):
    class Meta:
        model = DeviceLog
        fields = ["device","employee","checkout_date","chekin_date","condition_at_checkout_day","condition_at_checkin_day",
                  "comment"]
        required_fields = ["device","employee","checkout_date","condition_at_checkout_day",]
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Device Name'
                }),
        }