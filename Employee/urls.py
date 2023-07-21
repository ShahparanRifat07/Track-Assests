from django.urls import path
from .views import (add_employee)

app_name ='Employee'
urlpatterns = [
    path('add/',add_employee,name="add-employee"),
]