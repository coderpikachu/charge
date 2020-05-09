from django.shortcuts import render
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
def home_view(request,*args,**kwargs):
	return render(request,"home.html",{})

class LogInView(FormView):
    template_name='LogIn.html'
    form_class=LogInForm
    success_url=''

def logIn_view(request,*args,**kwargs):
    form=LogInForm(None or request.POST)
    print(1)
    if request.method == "POST":    
        print(2)
        print(form)
        if form.is_valid():
            try:   
                print(3)
                print(form.cleaned_data)
                my_id=form.cleaned_data['uId']
                my_pwd=form.cleaned_data['pwd']
                all_entries = User.objects.all()
                print(all_entries)
                print(User.objects.filter(id=my_id))
                print(User.objects.filter(id=my_id,my_pwd='pwd').len)
                if(User.objects.filter(id=my_id,my_pwd='pwd').len==1):
                    return redirect(f"{my_id}/{pwd}/home")  

            except:  
                pass  
    return render(request,"logIn.html",{'form':form})  

def signUp_view(request,*args,**kwargs):
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/logIn/')  
            except:  
                pass  
    else:  
        form = UserForm()
    return render(request,"signUp.html",{'form':form})  