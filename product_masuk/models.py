from django.db import models

# Create your models here.
class ProductMasuk(models.Model):
    name_bahan = models.CharField(max_length=200, db_index=True)
    name_supplier = models.CharField(max_length=200, db_index=True)
    address = models.TextField(blank=True)
    total = models.IntegerField()
    satuan = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_bahan