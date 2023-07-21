from django.urls import path
from .views import add_device,add_device_log

app_name ='Device'
urlpatterns = [
    path('add/',add_device,name="add-device"),
    path('device-log/add',add_device_log,name="add-device-log"),
]