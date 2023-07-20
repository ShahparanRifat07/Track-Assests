from django.urls import path
from .views import (create_company)

app_name ='Company'
urlpatterns = [
    path('create/',create_company,name="create-company"),
]