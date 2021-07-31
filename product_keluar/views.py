from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductKeluar
from .forms import ProductKeluarForm

# Create your views here.
def AddProductKeluar(request):
    form = ProductKeluarForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/product_keluar/bahan/")
    context = {
        "form": form,
    }
    return render(request, 'product_keluar/form.html' , context)

def product_keluars(request):
    product_keluars = ProductKeluar.objects.all()
    context = {
        "product_keluars": product_keluars,
    }
    return render(request, 'product_keluar/product_keluars.html', context)

def delete(request, id):
	instance = get_object_or_404(ProductKeluar, id=id)
	instance.delete()
	#messages.success(request, "Successfully Deleted")
	return redirect("/product_keluar/bahan/")
