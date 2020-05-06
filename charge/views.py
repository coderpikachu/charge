from django.shortcuts import render, redirect  
from charge.forms import ChargeForm  
from charge.models import Charge  
# Create your views here.  
def ch(request):  
    if request.method == "POST":  
        form = ChargeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/charge/show')  
            except:  
                pass  
    else:  
        form = ChargeForm()  
    return render(request,'charge/index.html',{'form':form})  
def show(request):  
    charges = Charge.objects.all()  
    return render(request,"charge/show.html",{'charges':charges})  
def edit(request, id):  
    charge = Charge.objects.get(id=id)  
    return render(request,'charge/edit.html', {'charge':charge})  
def update(request, id):  
    charge = Charge.objects.get(id=id)  
    form = ChargeForm(request.POST, instance = charge)  
    if form.is_valid():  
        form.save()  
        return redirect("/charge/show")  
    return render(request, 'charge/edit.html', {'charge': charge})  
def destroy(request, id):  
    charge = Charge.objects.get(id=id)  
    charge.delete()  
    return redirect("/charge/show")  