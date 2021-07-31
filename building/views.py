from django.db.models import query
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product 
from cart.forms import CartAddProductForm
from .forms import ProductForm, CategoryForm

# def home(request):
# 	return render(request, 'home.html')

def AddProduct(request):
    #if not request.user.is_staff or not request.user.is_superuser:
    	#raise Http404

    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.available = True
    	instance.save()
    	# message success 
    	#message.success(request, "Successfully")
    	return redirect("/products")
    context = {
    	"form": form,
    }
    return render(request, 'building/product/form.html', context)

def product_list(request, category_slug=None):
	category =None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, 'building/product/list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	return render(request, 'building/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

def products(request):
	products = Product.objects.all()
	context = {
		"products":products
	}
	return render(request, 'building/product/products.html', context) 

def addcategory(request):
	form = CategoryForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success 
		# message.success(requidest, "Successfully")
		return redirect("/categories")
	context = {
		"form": form,
	}
	return render(request, 'building/category.html', context)

def product(request, id):
	product = get_object_or_404(Product, id=id)
	context = {
		"product": product,
	}
	return render(request, 'building/product/product.html', context)

def update(request, id):
	instance = get_object_or_404(Product, id=id)
	form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("/products" )
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'building/product/form.html', context)

def delete(request, id):
	instance = get_object_or_404(Product, id=id)
	instance.delete()
	#messages.success(request, "Successfully Deleted")
	return redirect("/products")

def update_category(request, id):
	instance = get_object_or_404(Category, id=id)
	form = CategoryForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("/categories" )
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'building/category.html', context)

def delete_category(request, id):
	instance = get_object_or_404(Category, id=id)
	instance.delete()
	#messages.success(request, "Successfully Deleted")
	return redirect("/categories")

def categories(request):
	categories = Category.objects.all()
	context = {
		"categories": categories,
	}
	return render(request, 'building/categories.html', context)

def list_category(request, id):
	category = get_object_or_404(Category, id=id)
	context = {
		"category": category,
	}
	return render(request, 'building/list_category.html', context)
	
