from django.urls import path
from myapp import views

urlpatterns = [
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('aggregate/', views.aggregate_data, name='aggregate-data'),
]
