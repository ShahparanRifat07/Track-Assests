"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Account.urls',namespace='Account')),
    path('company/',include('Company.urls',namespace='Company')),
    path('company/employee/',include('Employee.urls',namespace='Employee')),
    path('company/device/',include('Device.urls',namespace='Device')),
    path('subscription/',include('Subscription.urls',namespace='Subscription')),


    #API
    path('api/user/',include('Account.api.urls',namespace='Account')),
    path('api/company/',include('Company.api.urls',namespace='Company')),
    path('api/company/employee/',include('Employee.api.urls',namespace='Employee')),
    path('api/company/device/',include('Device.api.urls',namespace='Device')),
]
