from django.core.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps
from .models import Device
from Employee.models import Employee
from Company.models import Company


def staff_or_manager_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # try:
                if Company.objects.filter(company_manager = request.user):
                    request.type = "Company"
                    return view_func(request,*args,**kwargs)
                elif Employee.objects.filter(user = request.user,is_staff = True):
                    request.type = "Employee"
                    return view_func(request,*args,**kwargs)
                else:
                    raise PermissionDenied
            # except ObjectDoesNotExist:
            #     return HttpResponse("Forbidden",status=403)
        else:
            return redirect('Account:login')
    return wrapped_view



def product_active_required(view_func):
    @wraps(view_func)
    def wrapped_view(request,id, *args, **kwargs):
        try:
            device = Device.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse("Page Not Found",status=404)
        if device.active == True:
            return view_func(request,id,*args,**kwargs)
        else:
            messages.add_message(request, messages.INFO, "Product isn't active")
            return redirect('Device:device-list')
    return wrapped_view


def premium_subscription_required(view_func):
    @wraps(view_func)
    def wrap(request,*args,**kwargs):
        try:

            if request.type == "Company":
                employee_count = Employee.objects.filter(company = request.user.company_manager).count()
                if not request.user.company_manager.premium and employee_count>=1000:
                    return HttpResponse("You need to upgrade to premium plan to add more employee")
                else:
                    return view_func(request,*args,**kwargs)
            elif request.type == "Employee":
                employee_count = Employee.objects.filter(company = request.user.employee.employee_company).count()
                if not request.user.employee.employee_company.premium and employee_count>=1000:
                    return HttpResponse("You need to upgrade to premium plan to add more employee")
                else:
                    return view_func(request,*args,**kwargs)         
            else:
                return HttpResponse("What the hack are you doing here")

        except ObjectDoesNotExist:
            messages.add_message(request, messages.INFO, "Create a Company account to access")
            return redirect('Account:login')   
    return wrap



