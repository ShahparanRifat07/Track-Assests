from django.urls import path
from .views import add_device,check_out_device,device_list

app_name ='Device'
urlpatterns = [
    path('add/',add_device,name="add-device"),
    path('list/',device_list,name="device-list"),
    path('check-out',check_out_device,name="checkout-device"),
]