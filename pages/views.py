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
    id=kwargs['my_id']
    val=User.objects.filter(uId=id).first()
    print(val.types)
    return render(request,"pages/home.html",{'my_id':id,'types':val.types})


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
        ordinary_dict={}
        if request.POST.__getitem__('types')=='C':
            ordinary_dict = {'student_add':False,'student_edit':False,'student_delete':False,
            'flat_add':False,'flat_edit':False,'flat_delete':False,
            'dormitory_add':False,'dormitory_edit':False,'dormitory_delete':False,
            'charge_add':False,'charge_edit':False,'charge_delete':False,
            'user_add':False,'user_edit':False,'user_delete':False,} 
        elif request.POST.__getitem__('types')=='S':
            ordinary_dict = {'student_add':True,'student_edit':True,'student_delete':True,
            'flat_add':True,'flat_edit':True,'flat_delete':True,
            'dormitory_add':True,'dormitory_edit':True,'dormitory_delete':True,
            'charge_add':True,'charge_edit':True,'charge_delete':True,
            'user_add':True,'user_edit':True,'user_delete':True,} 
        else:
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