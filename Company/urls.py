from django.urls import path
from .views import (create_company,dashboard)

app_name ='Company'
urlpatterns = [
    path('create/',create_company,name="create-company"),
    path('dashboard/',dashboard,name="dashboard-company"),
]