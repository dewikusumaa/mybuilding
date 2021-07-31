from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductMasuk
from .forms import ProductMasukForm

# Create your views here.
def AddProductMasuk(request):
    form = ProductMasukForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/product_masuk/list/")
    context = {
        "form": form,
    }
    return render(request, 'product_masuk/form.html' , context)

def product_masuks(request):
    product_masuks = ProductMasuk.objects.all()
    context = {
        "product_masuks": product_masuks,
    }
    return render(request, 'product_masuk/product_masuks.html', context)

def delete(request, id):
	instance = get_object_or_404(ProductMasuk, id=id)
	instance.delete()
	#messages.success(request, "Successfully Deleted")
	return redirect("/product_masuk/list/")
