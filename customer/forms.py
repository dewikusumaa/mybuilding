# form customer 
# validasi customer dengan nama (django validasi name)

from django import forms
from .models import Customer 

class CustomerForm(forms.ModelForm):
    cust_kode = forms.CharField()
    name    = forms.CharField()
    no_hp   = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ('cust_kode', 'name', 'no_hp', 'address')
        model = Customer 