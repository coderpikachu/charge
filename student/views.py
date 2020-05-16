from django.shortcuts import render, redirect ,get_object_or_404
from student.forms import StudentForm  
from student.models import Student 
from flat.models import Flat 
from user.models import User 
from django.http import *
from django import forms 
import json
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )
from django_filters.views import FilterView
from .filters import StudentFilter
# Create your views here.  
class Create_View(CreateView):
    template_name='student/create.html'
    form_class=StudentForm
    queryset=Student.objects.all()
    success_url='../../student/filterList/'
    my_id=''
    my_pwd=''
    request=None
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        return context

    def form_invalid(self,form,*args,**kwargs):
        self.my_id=str(self.request.get_full_path()).split('/')[1:2][0]
        return super().form_invalid(form)

    def form_valid(self,form,*args,**kwargs):
        string=str(self.request.get_full_path()).split('/')[1:3]
        val=User.objects.filter(uId=self.my_id).values()
        return super().form_valid(form)

class CreateOnly_View(CreateView):
    template_name='student/createOnly.html'
    form_class=StudentForm
    queryset=Student.objects.all()
    success_url='../../student/filterList/'
    my_id=''
    my_pwd=''
    request=None
    def get_initial(self,*args,**kwargs):
        return { 'sId': self.my_id}
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        return context

    def form_invalid(self,form,*args,**kwargs):
        self.my_id=str(self.request.get_full_path()).split('/')[1:2][0]
        return super().form_invalid(form)

    def form_valid(self,form,*args,**kwargs):
        string=str(self.request.get_full_path()).split('/')[1:3]
        val=User.objects.filter(uId=self.my_id).values()
        print(form)
        return super().form_valid(form)

def filterListView(request,*args,**kwargs):
    authority=User.objects.filter(uId=kwargs['my_id']).first()
    student_add=authority.student_add
    student_edit=authority.student_edit
    student_delete=authority.student_delete
    filter = StudentFilter(request.GET, queryset=Student.objects.all())
    return render(request, 'student/filterList.html', {'filter': filter,'my_id':kwargs['my_id'],'student_add':student_add,
        'student_edit':student_edit,'student_delete':student_delete})

class Update_View(UpdateView):
    template_name='student/update.html'
    form_class=StudentForm
    queryset=Student.objects.all()
    success_url='../../filterList/'

    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        return context

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Student,sId=id_)

    def form_invalid(self,form,*args,**kwargs):
        self.my_id=str(self.request.get_full_path()).split('/')[1:2][0]
        return super().form_invalid(form)
        

    def form_valid(self,form):
        return super().form_valid(form)

class Delete_View(DeleteView):
    template_name='student/delete.html'
    success_url='../../filterList/'

    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        return context

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Student,sId=id_)