from django.shortcuts import render, redirect  
from dormitory.forms import DormitoryForm  
from dormitory.models import Dormitory  
# Create your views here.  
def dormi(request):  
    if request.method == "POST":  
        form = DormitoryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = DormitoryForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    dormitories = Dormitory.objects.all()  
    return render(request,"show.html",{'dormitories':dormitories})  
def edit(request, id):  
    dormitory = Dormitory.objects.get(id=id)  
    return render(request,'edit.html', {'dormitory':dormitory})  
def update(request, id):  
    dormitory = Dormitory.objects.get(id=id)  
    form = DormitoryForm(request.POST, instance = dormitory)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'dormitory': dormitory})  
def destroy(request, id):  
    dormitory = Dormitory.objects.get(id=id)  
    dormitory.delete()  
    return redirect("/show")  