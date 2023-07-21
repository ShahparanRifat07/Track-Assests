from django.urls import path
from .views import (add_employee,employee_list)

app_name ='Employee'
urlpatterns = [
    path('add/',add_employee,name="add-employee"),
    path('list/',employee_list,name="employee-list"),
]