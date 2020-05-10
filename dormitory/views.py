from django.shortcuts import render, redirect  
from dormitory.forms import DormitoryForm  
from dormitory.models import Dormitory  
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )
# Create your views here.  
class DorCreateView(CreateView):
    template_name='dormitory/index.html'
    form_class=DormitoryForm
    queryset=Dormitory.objects.all()
    success_url='/dormitory/show'
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
def dor(request):  
    if request.method == "POST":  
        form = DormitoryForm(request.POST)  
        print(form)
        print(1)
        if form.is_valid():  
            print(form.cleaned_data)
            try:  
                print(2)
                form.save()  
                return redirect('/dormitory/show')  
            except:  
                pass  
    else:  
        form = DormitoryForm()  
    return render(request,'dormitory/index.html',{'form':form})  
def show(request):  
    dormitories = Dormitory.objects.all()  
    return render(request,"dormitory/show.html",{'dormitories':dormitories})  
def edit(request, id):  
    dormitory = Dormitory.objects.get(id=id)  
    return render(request,'dormitory/edit.html', {'dormitory':dormitory})  
def update(request, id):  
    dormitory = Dormitory.objects.get(id=id)  
    form = DormitoryForm(request.POST, instance = dormitory)  
    if form.is_valid():  
        form.save()  
        return redirect("/dormitory/show")  
    return render(request, 'dormitory/edit.html', {'dormitory': dormitory})  
def destroy(request, id):  
    dormitory = Dormitory.objects.get(id=id)  
    dormitory.delete()  
    return redirect("/dormitory/show")  