from django.contrib import admin
from .models import ProductMasuk

# Register your models here.
@admin.register(ProductMasuk)
class ProductMasukAdmin(admin.ModelAdmin):
    list_display = ['name_bahan', 'name_supplier', 'address', 'total', 'satuan', 'created', 'updated']
    list_filter =['created', 'updated']
