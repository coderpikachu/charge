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
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = FlatForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    flats = Flat.objects.all()  
    return render(request,"show.html",{'flats':flats})  
def edit(request, id):  
    flat = Flat.objects.get(id=id)  
    return render(request,'edit.html', {'flat':flat})  
def update(request, id):  
    flat = Flat.objects.get(id=id)  
    form = FlatForm(request.POST, instance = flat)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'flat': flat})  
def destroy(request, id):  
    flat = Flat.objects.get(id=id)  
    flat.delete()  
    return redirect("/show")  