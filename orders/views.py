from building.models import Product
from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart 
# from product_keluar.models import ProductKeluar


def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		# keluar = ProductKeluar(category=['category'], product=['product'], total=['total'])
		# keluar.save()
		if form.is_valid():
			order = form.save()
			for item in cart:
				print(item)
				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
				# product=item['product']
				# p = get_object_or_404(Product, name=product)
				# q =item['quantity'] 
				# sisa = p.stock - q 
				# s = Product(stock=sisa)
				# s.save()
			# clear the cart
			cart.clear()
			context = {
				"order": order,
				"cart": cart, 
			}
			return render(request, 'orders/created.html', context)

	else:
		form = OrderCreateForm()
		return render(request, 'orders/create.html', {'cart': cart, 'form':form})

def orders(request):
	orders = OrderItem.objects.all()
	context = {
		"orders": orders,
	}
	return render(request, 'orders/order.html', context)
