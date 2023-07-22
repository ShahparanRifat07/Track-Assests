from django.urls import path
from .views import subscribe_session,success_view,cancel_view,stripe_webhook

app_name ='Subscription'
urlpatterns = [
    path('cancel/', cancel_view, name='cancel'),
    path('success/', success_view, name='success'),
    path('create-checkout-session/<int:id>/', subscribe_session, name='create-checkout-session'),
    path('webhooks/stripe/',stripe_webhook,name='stripe-webhook')
]