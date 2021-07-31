from datetime import datetime
from decimal import Decimal 
from django.conf import settings
from building.models import Product
from datetime import datetime

class Cart(object):
	def __init__(self, request):
		"""
		Inisialisasi gerobak
		"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# simpan keranjang kosong di sesi
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity=1, override_quantity=False):
		"""
		Tambahkan produk ke keranjang atau perbarui jumlahnya.
		"""
		product_id = str(product.id)
		if product_id not in self.cart:
			now = datetime.now()
			self.cart[product_id] = {'quantity':0, 'price': str(product.price)}

		if override_quantity:
			self.cart[product_id] ['quantity'] = quantity
		else:
			self.cart[product_id] ['quantity'] += quantity
		self.save()

	def save(self):
		# tandai sesi sebagai "diubah" untuk memastikannya disimpan
		self.session.modified = True

	def remove(self, product):
		"""
		Hapus produk dari keranjang.
		"""
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		"""
		Ulangi item di keranjang dan dapatkan produk dari database
		"""
		product_ids = self.cart.keys()
		# dapatkan objek produk dan tambahkan ke keranjang
		products = Product.objects.filter(id__in=product_ids)

		cart = self.cart.copy()
		for product in products:
			cart[str(product.id)] ['product'] = product

		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		"""
		Hitung semua item di gerobak
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		# keluarkan keranjang dari sesi.
		del self.session[settings.CART_SESSION_ID]
		self.save()