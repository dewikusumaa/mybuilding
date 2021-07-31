from django.contrib import admin
from .models import ProductKeluar

# Register your models here.
@admin.register(ProductKeluar)
class ProductKeluarAdmin(admin.ModelAdmin):
    list_display = ['category', 'product', 'total', 'satuan', 'created', 'updated']
    list_filter = ['created', 'updated']