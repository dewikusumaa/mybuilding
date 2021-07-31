from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from building.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from datetime import datetime, timedelta

@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	# if request.method == 'POST':
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		now = datetime.now()
		cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
		print(cart)
		return redirect('cart:cart_detail')
	# else:
	# 	form = CartAddProductForm()
	
	

@require_POST
def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')
	
def cart_detail(request):
	cart = Cart(request)
	now = datetime.now()
	jam = timedelta(hours=24)
	for item in cart:
		# h = item['timed']
		# print(h)
		# j = h + str(jam)
		# print(j)
		# if j < h: 
		# 	print(now)
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})

	context = {
		"cart": cart, 
	} 
	return render(request, 'cart/detail.html', context)