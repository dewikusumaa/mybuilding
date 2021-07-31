from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cust_kode', 'name', 'no_hp', 'address', 'created', 'updated']
    list_filter = ['created', 'updated']