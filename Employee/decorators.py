from django.core.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from Employee.models import Employee

def manager_required(view_func):
    @wraps(view_func)
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.company_manager:
                    return view_func(request,*args,**kwargs)
                else:
                    raise PermissionDenied
            except ObjectDoesNotExist:
                messages.add_message(request, messages.INFO, "Create a Company account to access")
                return redirect('Company:create-company')
        else:
            return redirect('Account:login')
        
    return wrap


def stuff_required(view_func):
    @wraps(view_func)
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.employee.is_staff:
                    return view_func(request,*args,**kwargs)
                else:
                    raise PermissionDenied
            except ObjectDoesNotExist:
                messages.add_message(request, messages.INFO, "Create a Company account to access")
                return redirect('Account:login')
        else:
            return redirect('Account:login')
        
    return wrap


def premium_subscription_required(view_func):
    @wraps(view_func)
    def wrap(request,*args,**kwargs):
        try:
            employee_count = Employee.objects.filter(company = request.user.company_manager).count()
            if not request.user.company_manager.premium and employee_count>=1000:
                return HttpResponse("You need to upgrade to premium plan to add more employee")
            else:
                return view_func(request,*args,**kwargs)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.INFO, "Create a Company account to access")
            return redirect('Account:login')   
    return wrap