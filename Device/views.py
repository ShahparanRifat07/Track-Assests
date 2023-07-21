from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DeviceForm,DeviceLogForm
from .models import  Device,DeviceLog
# Create your views here.

def add_device(request):
    
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = Device()
            device.name = form.cleaned_data['name']
            device.condition = form.cleaned_data['condition']
            device.available = form.cleaned_data['available']
            device.company = request.user.company_manager
            device.save()

            return redirect('Device:add-device')
    
    elif request.method == "GET":
        form = DeviceForm()
        context = {
            'form': form,
        }
        return render(request,'device/add_device.html',context)
    else:
        return HttpResponse("Request Method not allowed")
    

def add_device_log(request):
    form = DeviceLogForm()
    context = {
        'form': form,
    }
    return render(request,'device/add_device.html',context)