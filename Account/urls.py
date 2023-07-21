from django.urls import path
from .views import (account_login,account_logout,home)

app_name ='Account'
urlpatterns = [
    path('',home,name="home"),
    path('login/',account_login,name="login"),
    path('logout/',account_logout,name="logout"),
]