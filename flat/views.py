from django.shortcuts import render, redirect  
from flat.forms import FlatForm  
from flat.models import Flat  
# Create your views here.  
def fl(request):  
    if request.method == "POST":  
        form = FlatForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/flat/show')  
            except:  
                pass  
    else:  
        form = FlatForm()  
    return render(request,'flat/index.html',{'form':form})  
def show(request):  
    flats = Flat.objects.all()  
    return render(request,"flat/show.html",{'flats':flats})  
def edit(request, id):  
    flat = Flat.objects.get(id=id)  
    return render(request,'flat/edit.html', {'flat':flat})  
def update(request, id):  
    flat = Flat.objects.get(id=id)  
    form = FlatForm(request.POST, instance = flat)  
    if form.is_valid():  
        form.save()  
        return redirect("/flat/show")  
    return render(request, 'flat/edit.html', {'flat': flat})  
def destroy(request, id):  
    flat = Flat.objects.get(id=id)  
    flat.delete()  
    return redirect("/flat/show")  