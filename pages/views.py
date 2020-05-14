from django.shortcuts import render,redirect
from django.http import HttpResponse
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
def home_view(request,my_id,*args,**kwargs):
    print(my_id)
    return render(request,"pages/home.html",{'my_id':my_id})

class LogInView(FormView):
    template_name='LogIn.html'
    form_class=LogInForm
    success_url=''

def logIn_view(request,*args,**kwargs):
    form=LogInForm(None or request.POST)
    if request.method == "POST":    
        if form.is_valid():
            try:   
                my_id=form.cleaned_data['uId']
                print(User.objects.filter(uId=my_id).count())
                if User.objects.filter(uId=my_id).count()>=1:
                    return redirect(f"{my_id}/home/")  

            except:  
                pass  
    return render(request,"pages/logIn.html",{'form':form})  

def signUp_view(request,*args,**kwargs):
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('../')  
            except:  
                pass  
    else:  
        form = UserForm()
    return render(request,"pages/signUp.html",{'form':form})  