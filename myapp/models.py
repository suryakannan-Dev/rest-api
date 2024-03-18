from django.db import models

class Customer(models.Model):
    CustomerId = models.CharField(max_length=15)
    Customerfirstname = models.CharField(max_length=50)
    Customerlastname = models.CharField(max_length=50)
    Customerdob = models.DateField()

class Payment(models.Model):
    Paymentid = models.CharField(max_length=15)
    Paymentcard = models.CharField(max_length=16)
    Paymentcvv = models.CharField(max_length=3)
    Paymenttransactionid = models.CharField(max_length=50)
