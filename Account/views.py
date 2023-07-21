from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.company_manager:
            return redirect("Company:dashboard-company")
    else:
        return render(request,'index.html')


def account_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(email= email,password = password)

            if user is not None:  
                if user.company_manager:
                    login(request,user)
                    return redirect("Company:dashboard-company")
            else:
                messages.add_message(request, messages.INFO, "No User Found")
                return redirect("Account:login")
            
        elif request.method == "GET":
            return render(request, 'account/login.html')
        else:
            return HttpResponse("Request Method not allowed")
    else:
        return redirect("Company:dashboard-company")
    

def account_logout(request):
    logout(request)
    return redirect('Account:login')
