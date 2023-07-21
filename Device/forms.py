from .models import Device,DeviceLog
from django.forms import ModelForm, TextInput,DateInput

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

        
