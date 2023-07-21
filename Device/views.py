from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,HttpResponseNotAllowed,Http404
from django.contrib import messages
from .forms import DeviceForm
from .models import  Device,DeviceLog
from Employee.models import Employee
from .decorators import manager_required
from django.utils import timezone
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
        return HttpResponse("Request Method not allowed",status = 405)


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

            return redirect('Device:device-list')
    
    elif request.method == "GET":
        form = DeviceForm()
        context = {
            'form': form,
        }
        return render(request,'device/add_device.html',context)
    else:
        return HttpResponse("Request Method not allowed",status = 405)
    

@manager_required
def check_out_device(request,id):
    try:
        device = Device.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Page Not Found",status=404)
    
    if request.method == "POST":
        if device.available == True:
            try:
                received_employee = request.POST.get("employee_id")
                employee = Employee.objects.get(id = received_employee)
            except ObjectDoesNotExist:
                return HttpResponse("Employee Does not exists",status = 404)
        
            log = DeviceLog(device = device,employee = employee,condition_at_checkout_day = device.condition)
            log.checkout_date = timezone.now().date().isoformat()
            log.save()
            return redirect('Device:device-list')
        else:
            messages.add_message(request, messages.INFO, "Device is currently not available")
            return redirect('Device:device-list')
        
    elif request.method == "GET":
        if device.available == True:
            employees = Employee.objects.select_related('employee_company').filter(employee_company = request.user.company_manager)
            context = {
                'device' : device,
                'employees' : employees,
            }
            return render(request,'device/checkout_device.html',context)
        else:
            messages.add_message(request, messages.INFO, "Device is currently not available")
            return redirect('Device:device-list')
    else:
        return HttpResponse("Request Method not allowed",status = 405)
    


@manager_required
def check_in_device(request,id):
    try:
        device = Device.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Page Not Found",status=404)
    if request.method == "POST":
        pass
    elif request.method == "GET":
        context = {
            'device' : device,
        }
        return render(request,'device/checkin_device.html',context)
    else:
        return HttpResponse("Request Method not allowed",status = 405)
    