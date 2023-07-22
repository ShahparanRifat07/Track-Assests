from django.urls import path
from .views import add_device,check_out_device,device_list,check_in_device,device_log_list

app_name ='Device'
urlpatterns = [
    path('add/',add_device,name="add-device"),
    path('list/',device_list,name="device-list"),
    path('check-out/<int:id>',check_out_device,name="checkout-device"),
    path('check-in/<int:id>',check_in_device,name="checkin-device"),
    path('log/<int:id>',device_log_list,name="device-log"),
]