from django.urls import path
from . import views

app_name = 'building'

urlpatterns = [
	path('edit/<int:id>', views.update_category),
	path('hapus/<int:id>', views.delete_category),
	path('list/<int:id>', views.list_category),
	path('categories/', views.categories),
	path('products/', views.products),
	path('add/', views.AddProduct),
	path('category/', views.addcategory),
	path('update/<int:id>', views.update),
	path('delete/<int:id>', views.delete),
	path('products/<int:id>', views.product),
	path('', views.product_list, name='product_list'),
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]