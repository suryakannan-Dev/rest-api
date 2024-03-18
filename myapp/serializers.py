from rest_framework import serializers
from myapp.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'CustomerId', 'Customerfirstname', 'Customerlastname', 'Customerdob']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'Paymentid', 'Paymentcard', 'Paymentcvv', 'Paymenttransactionid']
