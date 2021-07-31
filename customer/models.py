from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_kode = models.CharField(max_length=5)
    name = models.CharField(max_length=200, db_index=True)
    no_hp = models.CharField(max_length=13)
    address = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.cust_kode