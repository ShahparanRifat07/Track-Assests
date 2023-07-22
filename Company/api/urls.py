from django.urls import path
from .views import company_list,company_detail
app_name ='Company'
urlpatterns = [
    path('list/',company_list,name="company-list"),
    path('detail/<int:pk>',company_detail,name="company-detail"),
]