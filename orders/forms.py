from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	name = forms.CharField()
	no_hape = forms.CharField()
	address = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Order
		fields = ['name', 'no_hape', 'address']


		 