from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('delete/<int:id>/', views.delete_customer, name='delete_customer'),
    path('update/<int:id>/', views.update_customer, name='update_customer'),
    path('tambah/', views.AddCustomer),
    path('list/', views.customers),
]