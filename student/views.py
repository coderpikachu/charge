from django.shortcuts import render, redirect,get_object_or_404
from student.forms import StudentForm  
from student.models import Student  
from django.urls import reverse
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )
class StuCreateView(CreateView):
    template_name='student/index.html'
    form_class=StudentForm
    queryset=Student.objects.all()
    success_url='../student/show'
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class StuListView(ListView):
    template_name='student/show.html'
    queryset=Student.objects.all()

class StuUpdateView(UpdateView):
    template_name='student/edit.html'
    form_class=StudentForm
    queryset=Student.objects.all()
    success_url='../../show'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Student,sId=id_)
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class StuDeleteView(DeleteView):
    template_name='student/delete.html'
    success_url='../../show'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Student,sId=id_)