from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DeviceForm
from .models import  Device
from .decorators import manager_required
# Create your views here.



@manager_required
def device_list(request):
    if request.method == "GET":
        devices = Device.objects.select_related('company').filter(company=request.user.company_manager)
        context = {
            'devices' : devices,
        }
        return render(request, 'device/device_list.html',context)
    else:
        return HttpResponse("Request Method not allowed")


@manager_required
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
    

def check_out_device(request):
    form = DeviceLogForm(request.user.company_manager)
    context = {
        'form': form,
    }
    return render(request,'device/add_device_log.html',context)