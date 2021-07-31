from django.contrib import admin 
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('home/', views.index),
	path('product_masuk/', include('product_masuk.urls', namespace='product_masuk')),
	path('supplier/', include('supplier.urls', namespace='supplier')),
	path('product_keluar/', include('product_keluar.urls', namespace='product_keluar')),
	# path('accounts/', include('accounts.urls', namespace='accounts')),
	# path('customer/', include('customer.urls', namespace='customer')),
	path('orders/', include('orders.urls', namespace='orders')),
	path('cart/', include('cart.urls', namespace='cart')),
	path('', include('building.urls', namespace='building')),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)