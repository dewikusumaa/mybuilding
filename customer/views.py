from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm
 

# Create your views here.

# create customer 
def AddCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/customer/list/")
    context = {
        "form": form,
    }
    return render(request, 'customer/form.html' , context)

# list customer
def customers(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers,
    }
    return render(request, 'customer/customers.html', context)

def update_customer(request, id):
	instance = get_object_or_404(Customer, id=id)
	form = CustomerForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("/customer/list/")
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'customer/form.html', context)

def delete_customer(request, id):
	instance = get_object_or_404(Customer, id=id)
	instance.delete()
	#messages.success(request, "Successfully Deleted")
	return redirect("/customer/list/")