from django.urls import path
from .views import (add_employee,employee_list,staff_dashboard)

app_name ='Employee'
urlpatterns = [
    path('staff/dashboard',staff_dashboard,name="staff-dashboard"),
    path('add/',add_employee,name="add-employee"),
    path('list/',employee_list,name="employee-list"),
]