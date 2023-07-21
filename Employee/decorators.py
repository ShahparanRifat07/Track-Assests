from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect

def manager_required(view_fun):
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.company_manager:
                    return view_fun(request,*args,**kwargs)
                else:
                    raise PermissionDenied
            except:
                messages.add_message(request, messages.INFO, "Create a Company account to access")
                return redirect('Company:create-company')
        else:
            return redirect('Account:login')
        
    return wrap
