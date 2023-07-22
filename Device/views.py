from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,HttpResponseNotAllowed,Http404
from django.db.models import Q
from django.contrib import messages
from .forms import DeviceForm
from .models import  Device,DeviceLog
from Employee.models import Employee
from Company.models import Company
from .decorators import staff_or_manager_required,product_active_required
from django.utils import timezone
# Create your views here.



@staff_or_manager_required
def device_list(request):
    if request.method == "GET":
        if request.type =="Company":
            devices = Device.objects.select_related('company').filter(Q(company=request.user.company_manager) & Q(active=True))
        elif request.type == "Employee":
            devices = Device.objects.select_related('company').filter(Q(company=request.user.employee.employee_company) & Q(active=True))
        else:
            return HttpResponse("Forbidden",status=403)
        context = {
            'devices' : devices,
        }
        return render(request, 'device/device_list.html',context)
    else:
        return HttpResponse("Request Method not allowed",status = 405)





@staff_or_manager_required
def add_device(request): 
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = Device()
            device.name = form.cleaned_data['name']
            device.condition = form.cleaned_data['condition']
            device.active = form.cleaned_data['active']

            if request.type =="Company":
                device.company = request.user.company_manager
            elif request.type == "Employee":
                device.company = request.user.employee.employee_company
            else:
                return HttpResponse("Forbidden",status=403)

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
    


@staff_or_manager_required
def edit_device(request,id): 
    try:
        device = Device.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Page Not Found", status=404)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('Device:device-list')
    
    elif request.method == "GET":
        form = DeviceForm(data={
            'name' : device.name,
            'condition' : device.condition,
            'active' : device.active,
        })
        context = {
            'device' : device,
            'form': form,
        }
        return render(request,'device/edit_device.html',context)
    else:
        return HttpResponse("Request Method not allowed",status = 405)
    




@staff_or_manager_required
@product_active_required
def check_out_device(request,id):

    device = Device.objects.get(id=id)

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

            Device.objects.filter(id=id).update(available =False)

            return redirect('Device:device-list')
        else:
            messages.add_message(request, messages.INFO, "Device is currently not available")
            return redirect('Device:device-list')
        
    elif request.method == "GET":
        if device.available == True:
            if request.type == "Company":
                employees = Employee.objects.select_related('employee_company').filter(employee_company = request.user.company_manager)
            elif request.type == "Employee":
                employees = Employee.objects.select_related('employee_company').filter(employee_company = request.user.employee.employee_company)
            else:
                return HttpResponse("Forbidden",status=403)
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
    





@staff_or_manager_required
@product_active_required
def check_in_device(request,id):

    device = Device.objects.get(id=id)
    if request.method == "POST":
        if device.available == False:
            try:
                latest_device_log = DeviceLog.objects.filter(device=device, active=True,checkin_date=None).order_by('-checkout_date').first()
            except ObjectDoesNotExist:
                messages.add_message(request, messages.INFO, "Device needs to be chekout first")
                return redirect('Device:device-list')
            
            received_condition = request.POST.get("condition")
            received_comment = request.POST.get("comment")

            latest_device_log.checkin_date = timezone.now().date().isoformat()
            latest_device_log.condition_at_checkin_day = received_condition
            latest_device_log.comment = received_comment,
            latest_device_log.active = False
            latest_device_log.save()
            
            Device.objects.filter(id=id).update(available =True,condition = received_condition)
            return redirect('Device:device-list')
        else:
            messages.add_message(request, messages.INFO, "Device needs to be chekout first")
            return redirect('Device:device-list')
        
    elif request.method == "GET":
        if device.available == False:
            try:
                latest_device_log = DeviceLog.objects.filter(device=device, active=True,checkin_date=None).order_by('-checkout_date').first()
            except ObjectDoesNotExist:
                messages.add_message(request, messages.INFO, "Device needs to be chekout first")
                return redirect('Device:device-list')
            context = {
                'device' : device,
                'device_log':latest_device_log,
            }
            return render(request,'device/checkin_device.html',context)
        else:
            messages.add_message(request, messages.INFO, "Device needs to be chekout first")
            return redirect('Device:device-list')
    else:
        return HttpResponse("Request Method not allowed",status = 405)




@staff_or_manager_required
def device_log_list(request,id):
    if request.method == "GET":
        try:
            device = Device.objects.get(id = id)
        except ObjectDoesNotExist:
            return HttpResponse("Page Not Found",status=404)
        device_logs = DeviceLog.objects.select_related('device','employee').filter(device = device).order_by('-checkout_date')
        context ={
            'device' : device,
            'device_logs' : device_logs
        }
        return render(request,'device/log_device.html',context)
    else:
        return HttpResponse("Request Method not allowed",status = 405)