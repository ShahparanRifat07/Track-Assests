import stripe
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from decouple import config
from django.shortcuts import render, redirect
from Company.models import Company
from .decorators import company_required


@company_required
def subscription_home_page(request):
    company = Company.objects.get(company_manager = request.user.company_manager)
    context = {
        'company' : company,
    }
    return render(request,'subscription/checkout.html',context)

@company_required
def subscribe_session(request, id):
    stripe.api_key = config('STRIPE_PRIVATE_KEY')

    try:
        company = Company.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponse("Company Not Found",status=404)
    
    if settings.DEBUG:
        domain = "http://127.0.0.1:8000/subscription"
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1NWcHlAq14FaDrteIS0PbzDd',
            'quantity': 1,
        }],
        mode='payment',
        client_reference_id=str(company.id),
        metadata = {
            'company_id' : company.id
        },
        success_url= domain + '/'+'success/',
        cancel_url= domain + '/'+'cancel/',
    )
    return redirect(session.url)

@company_required
def success_view(request):
    return render(request,'subscription/success.html')

@company_required
def cancel_view(request):
    return render(request,'subscription/cancel.html')




@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, config('STRIPE_WEBHOOK_SECRET_KEY')
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        company_id = session["metadata"]["company_id"]
        session_id = event['id']

        company = Company.objects.get(id = company_id)
        company.stripe_product_id = session_id
        company.premium = True
        company.save()

        #Can send emaill after this by using customer_email
        
    return HttpResponse(status=200)