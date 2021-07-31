from django import forms
from .models import ProductMasuk

class ProductMasukForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        fields = ('name_bahan', 'name_supplier', 'address', 'total', 'satuan')
        model = ProductMasuk