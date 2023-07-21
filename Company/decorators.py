from django.core.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect,render

def manager_redirect(view_fun):
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.company_manager:
                    return redirect('Company:dashboard-company')
            except ObjectDoesNotExist:
                return view_fun(request,*args,**kwargs)
        else:
            return view_fun(request,*args,**kwargs)
    return wrap
