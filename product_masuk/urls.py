from django.urls import path
from . import views

app_name = 'product_masuk'

urlpatterns = [
    path('delete/<int:id>/', views.delete),
    path('add/', views.AddProductMasuk),
    path('list/', views.product_masuks),
]