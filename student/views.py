from django.shortcuts import render, redirect  
from student.forms import StudentForm  
from student.models import Student  
from django.urls import reverse
# Create your views here.  
def st(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/student/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,"index.html",{'form':form})  
def show(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})  
def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  
def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/student/show")  
    return render(request, 'edit.html', {'student': student})  
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/student/show")  