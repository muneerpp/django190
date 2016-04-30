from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
# Create your views here.

def get_customer_name(request):
    customer_details = Customer.objects.all()
    context = {
        
        "customer_details" :customer_details,
        
    }
    return render(request, "customer.html",context)