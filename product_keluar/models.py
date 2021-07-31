from django.db import models

# Create your models here.
class ProductKeluar(models.Model):
    category    = models.CharField(max_length=200, db_index=True)
    product     = models.CharField(max_length=200, db_index=True)
    total       = models.IntegerField()
    satuan      = models.CharField(max_length=50) 
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category