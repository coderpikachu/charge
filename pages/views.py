from django.shortcuts import render
from django.http import HttpResponse
# Create your models here.
def home_view(request,*args,**kwargs):
	return render(request,"home.html",{})

def logIn_view(request,*args,**kwargs):
	if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                id=form.clean_data('id')
                pwd=form.clean_data('pwd')
                return redirect('<id>/<pwd>/home')  
            except:  
                pass  
    else:  
        form = UserForm()
    return render(request,"logIn.html",{'form':form})  

def signUp_view(request,*args,**kwargs):
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = UserForm()
    return render(request,"signUp.html",{'form':form})  