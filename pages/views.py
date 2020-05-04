from django.shortcuts import render
from django.http import HttpResponse
# Create your models here.
def home_view(request,*args,**kwargs):
	my_context={
	"my_number":123,
	"my_list":[1,2,3]
	}
	return render(request,"home.html",my_context)