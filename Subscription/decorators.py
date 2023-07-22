from django.core.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect


def company_required(view_func):
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