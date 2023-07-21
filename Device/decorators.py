from django.core.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,HttpResponseNotAllowed,Http404
from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps
from .models import Device,DeviceLog

def manager_required(view_fun):
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.company_manager:
                    return view_fun(request,*args,**kwargs)
                else:
                    raise PermissionDenied
            except ObjectDoesNotExist:
                messages.add_message(request, messages.INFO, "Create a Company account to access")
                return redirect('Company:create-company')
        else:
            return redirect('Account:login')
        
    return wrap

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

