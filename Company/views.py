from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .helper import *
from .decorators import manager_redirect

from .models import Company


"""
Registering a company manually
This can be also done quickly and with much less code by using django forms 
"""

def dashboard(request):
    return render(request,'company/dashboard.html')

@manager_redirect
def create_company(request):
    if request.method == "POST":
        received_company_name = request.POST.get("company-name")
        received_company_email = request.POST.get("company-email")
        received_first_name = request.POST.get("first-name")
        received_last_name = request.POST.get("last-name")
        received_manager_email = request.POST.get("manager-email")
        received_password = request.POST.get("password")

        if isEmpty(
            received_company_name,received_company_email,received_first_name,received_last_name,
            received_manager_email,received_password
            ):
            messages.add_message(request, messages.INFO, "Empty Fields")
            return redirect('Company:create-company')
        
        else:
            if checkCompanyExists(received_manager_email) is True:
                messages.add_message(request, messages.INFO, "This manager email is already assigned to a company")
                return redirect('Company:create-company')
            else:
                company_obj = Company(company_name = received_company_name, company_email = received_company_email)
                company_obj._manager_first_name = received_first_name
                company_obj._manager_last_name = received_last_name
                company_obj._manager_email = received_manager_email
                company_obj._manager_password = received_password
                company_obj.save()
                return redirect('Account:login')

    elif request.method == "GET":
        return render(request,'company/register.html')
    else:
        return HttpResponse("Request Method not allowed",status = 405)
    


