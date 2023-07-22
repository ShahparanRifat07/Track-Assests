from .models import Device
from django.forms import ModelForm, TextInput

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ["name","condition","active"]
        required_fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Device Name'
                }),
        }

        
