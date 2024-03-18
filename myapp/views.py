from rest_framework import generics
from myapp.models import Customer, Payment
from myapp.serializers import CustomerSerializer, PaymentSerializer
from django.http import JsonResponse
import requests

class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

def aggregate_data(request):
    # Define the base URLs of the existing APIs
    base_url = 'http://127.0.0.1:8000/api/'

    # Fetch data from the customers API
    customers_response = requests.get(base_url + 'customers/')
    customers_data = customers_response.json()

    # Fetch data from the payments API
    payments_response = requests.get(base_url + 'payments/')
    payments_data = payments_response.json()

    # Convert payments data to a dictionary with ID as key
    payments_dict = {payment['id']: payment for payment in payments_data}

    # Merge data from both APIs under the same ID
    merged_data = {}
    for customer in customers_data:
        customer_id = customer['id']
        merged_data[customer_id] = customer.copy() 
        payment_data = payments_dict.get(customer_id, {})  
        merged_data[customer_id].update(payment_data)  

    return JsonResponse(merged_data)