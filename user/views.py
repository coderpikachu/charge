from django.shortcuts import render, redirect  
from user.forms import UserForm  
from user.models import User  
from django.urls import reverse
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )
# Create your views here.  
def u(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/user/show')  
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,"user/index.html",{'form':form})  
def show(request):  
    users = User.objects.all()  
    return render(request,"user/show.html",{'users':users})  
def edit(request, id):  
    user = User.objects.get(id=id)  
    return render(request,'user/edit.html', {'user':user})  
def update(request, id):  
    user = User.objects.get(id=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/user/show")  
    return render(request, 'user/edit.html', {'user': user})  
def destroy(request, id):  
    user = User.objects.get(id=id)  
    user.delete()  
    return redirect("/user/show")  