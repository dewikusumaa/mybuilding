from django.urls import path
from . import views

app_name = 'product_keluar'

urlpatterns = [
    path('delete/<int:id>/', views.delete),
    path('add/', views.AddProductKeluar),
    path('bahan/', views.product_keluars),
]