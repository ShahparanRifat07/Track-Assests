from django.urls import path
from .views import (account_login,account_logout)

app_name ='Account'
urlpatterns = [
    path('login/',account_login,name="login"),
    path('logout/',account_logout,name="logout"),
]