from django.shortcuts import render,redirect
from django.http import HttpResponse,QueryDict
from user.forms import UserForm
from user.models import User
from pages.forms import LogInForm
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )
from django.views.generic.edit import FormView
# Create your models here.
def homeView(request,*args,**kwargs):
    return render(request,"pages/home.html",{'my_id':kwargs['my_id']})


def logInView(request,*args,**kwargs):
    form=LogInForm(None or request.POST)
    if request.method == "POST":    
        if form.is_valid():
            try:   
                my_id=form.cleaned_data['uId']
                if User.objects.filter(uId=my_id).count()>=1:
                    return redirect(f"{my_id}/home/")  
            except:  
                pass  
    return render(request,"pages/logIn.html",{'form':form})  

def signUpView(request,*args,**kwargs):
    if request.method == "POST":  
        ordinary_dict = {'student_add':True,'student_edit':True,'student_delete':True,
            'flat_add':True,'flat_edit':True,'flat_delete':True,
            'dormitory_add':True,'dormitory_edit':True,'dormitory_delete':True,
            'charge_add':True,'charge_edit':True,'charge_delete':True,
            'user_add':False,'user_edit':False,'user_delete':False,} 
        query_dict = QueryDict('', mutable=True)
        query_dict.update(ordinary_dict)
        query_dict.update(request.POST)
        form = UserForm(query_dict)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('../')  
            except:  
                pass  
    else:  
        form = UserForm()
    return render(request,"pages/signUp.html",{'form':form})  