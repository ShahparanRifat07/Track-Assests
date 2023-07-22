from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .helper import *
from .models import Employee
from Company.models import Company
from .decorators import manager_required,stuff_required,premium_subscription_required
# Create your views here.

@stuff_required
def staff_dashboard(request):
    return render(request,'employee/staff_dashboard.html')

@manager_required
def employee_list(request):
    employees = Employee.objects.select_related('user').filter(employee_company=request.user.company_manager)
    context = {
        'employees' : employees,
    }
    return render(request, 'employee/employee_list.html',context)

@manager_required
@premium_subscription_required
def add_employee(request):
    if request.method == "POST":
        received_first_name = request.POST.get("first-name")
        received_last_name = request.POST.get("last-name")
        received_manager_email = request.POST.get("email")
        received_password = request.POST.get("password")
        received_is_staff = request.POST.get("is_staff")

        if isEmpty(received_first_name,received_last_name,
            received_manager_email,received_password
            ):
            messages.add_message(request, messages.INFO, "Empty Fields")
            return redirect('Employee:add-employee')
        
        else:
            if checkEmailExists(received_manager_email) is True:
                messages.add_message(request, messages.INFO, "This email is in use")
                return redirect('Employee:add-employee')
            else:
                company = Company.objects.select_related('company_manager').filter(company_manager=request.user).first()

                received_is_staff = True if received_is_staff == 'on' else False

                employee_obj = Employee(employee_company = company,is_staff = received_is_staff)

                employee_obj._first_name = received_first_name
                employee_obj._last_name = received_last_name
                employee_obj._email = received_manager_email
                employee_obj._password = received_password

                employee_obj.save()
                return redirect('Employee:employee-list')

    elif request.method == "GET":
        return render(request,'employee/add_employee.html')
    else:
        return HttpResponse("Request Method not allowed")
    

@manager_required
def edit_employee(request):
    pass


@manager_required
def delete_employee(request):
    pass


@manager_required
def employee_device_log(request):
    pass