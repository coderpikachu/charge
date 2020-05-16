from django.shortcuts import render, redirect ,get_object_or_404
from dormitory.forms import DormitoryForm  
from dormitory.models import Dormitory 
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
from .filters import DormitoryFilter
# Create your views here.  
class Create_View(CreateView):
    template_name='dormitory/create.html'
    form_class=DormitoryForm
    queryset=Dormitory.objects.all()
    success_url='../../dormitory/filterList/'
    my_id=''
    request=None
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        return super().get(self,request,*args,**kwargs)

    # def post(self,request,*args,**kwargs):
    #     print(request.POST)
    #     self.get(self,request,*args,**kwargs)
    #     print(args)
    #     print(kwargs)
    #     #self.form_class.clean_peopleNum(form,1)
    #     return self.form_valid(self,DormitoryForm(request.POST),*args,**kwargs)

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

def filterListView(request,*args,**kwargs):
    authority=User.objects.filter(uId=kwargs['my_id']).first()
    dormitory_add=authority.dormitory_add
    dormitory_edit=authority.dormitory_edit
    dormitory_delete=authority.dormitory_delete
    filter = DormitoryFilter(request.GET, queryset=Dormitory.objects.all())
    return render(request, 'dormitory/filterList.html', {'filter': filter,'my_id':kwargs['my_id'],'dormitory_add':dormitory_add,
        'dormitory_edit':dormitory_edit,'dormitory_delete':dormitory_delete})

class Update_View(UpdateView):
    template_name='dormitory/update.html'
    form_class=DormitoryForm
    queryset=Dormitory.objects.all()
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
        return get_object_or_404(Dormitory,dId=id_)
        
    def form_invalid(self,form,*args,**kwargs):
        self.my_id=str(self.request.get_full_path()).split('/')[1:2][0]
        return super().form_invalid(form)

    def form_valid(self,form):
        return super().form_valid(form)

class Delete_View(DeleteView):
    template_name='dormitory/delete.html'
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
        return get_object_or_404(Dormitory,dId=id_)