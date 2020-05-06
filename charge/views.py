from django.shortcuts import render, redirect  
from charge.forms import ChargeForm  
from charge.models import Charge  
# Create your views here.  
def cha(request):  
    if request.method == "POST":  
        form = ChargeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ChargeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    charges = Charge.objects.all()  
    return render(request,"show.html",{'charges':charges})  
def edit(request, id):  
    charge = Charge.objects.get(id=id)  
    return render(request,'edit.html', {'charge':charge})  
def update(request, id):  
    charge = Charge.objects.get(id=id)  
    form = ChargeForm(request.POST, instance = charge)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'charge': charge})  
def destroy(request, id):  
    charge = Charge.objects.get(id=id)  
    charge.delete()  
    return redirect("/show")  