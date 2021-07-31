from django.urls import path
from . import views

app_name = 'supplier'

urlpatterns = [
    path('deleteSupplier/<int:id>/', views.deleteSupplier),
    path('create/', views.createSupplier),
    path('listSupplier/', views.suppliers),
]