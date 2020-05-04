from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_detail_view(request,*args,**kwargs):
	obj=Product.objects.get(id=1)
	context={
	"title":obj.title,
	"description":obj.description,
	"price":obj.price
	}
	return render(request,"product/detail.html",context)

def product_create_view(request,*args,**kwargs):
	form=ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ProductForm(request.POST or None)
	context={
		"form":form
	}
	return render(request,"product/create.html",context)