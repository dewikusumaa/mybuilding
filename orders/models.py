from django.db import models
from building.models import Product
# from customer.models import Customer

class Order(models.Model):
	name 			= models.CharField(max_length=50)
	no_hape 		= models.CharField(max_length=13)
	address 		= models.CharField(max_length=250)
	# last_name 	= models.CharField(max_length=50)
	# email 		= models.EmailField()
	# postal_code = models.CharField(max_length=20)
	# city 		= models.CharField(max_length=100)
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	paid 		= models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return f'Order {self.id}'

	def get_total_cost(self):
		return sum(item.get_total_cost() for item in self.item.all())

class OrderItem(models.Model):
	order 		= models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product 	= models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price 		= models.DecimalField(max_digits=10, decimal_places=2)
	quantity 	= models.PositiveIntegerField(default=1)

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		return self.price * self.quantity