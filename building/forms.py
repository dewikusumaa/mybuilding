from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
	category 		= forms.ModelChoiceField(queryset=Category.objects.all())
	name 	 		= forms.CharField()
	slug 			= forms.CharField()
	image 			= forms.ImageField()
	description 	= forms.CharField(widget=forms.Textarea)
	price 			= forms.DecimalField()
	stock 			= forms.IntegerField()
	#available = forms.BooleanField(widget=forms.RadioSelect(choices=YES_NO))

	class Meta: 
		fields = ('category', 'name', 'slug', 'image','description', 'price', 'stock')
		model = Product

class CategoryForm(forms.ModelForm):
	name = forms.CharField()
	slug = forms.CharField()

	class Meta:
		fields = ('name', 'slug')
		model = Category
