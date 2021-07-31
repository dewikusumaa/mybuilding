from django import forms
from .models import ProductKeluar

class ProductKeluarForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'product', 'total', 'satuan')
        model = ProductKeluar