from django.shortcuts import render, redirect ,get_object_or_404
from charges.forms import ChargeForm
from charges.models import Charges 
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
from .filters import ChargeFilter
# Create your views here.  
class Create_View(CreateView):
    template_name='charges/create.html'
    form_class=ChargeForm
    queryset=Charges.objects.all()
    success_url='../../charges/filterList/'
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
        # string=str(self.request.get_full_path()).split('/')[1:3]
        # val=User.objects.filter(uId=self.my_id).values()
        return super().form_valid(form)

def filterListView(request,*args,**kwargs):
    authority=User.objects.filter(uId=kwargs['my_id']).first()
    charge_add=authority.charge_add
    charge_edit=authority.charge_edit
    charge_delete=authority.charge_delete
    filter = ChargeFilter(request.GET, queryset=Charges.objects.all())
    return render(request, 'charges/filterList.html', {'filter': filter,'my_id':kwargs['my_id'],'charge_add':charge_add,
        'charge_edit':charge_edit,'charge_delete':charge_delete})

class Update_View(UpdateView):
    template_name='charges/update.html'
    form_class=ChargeFilter
    queryset=Charges.objects.all()
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
        return get_object_or_404(Charges,cId=id_)

    def form_invalid(self,form,*args,**kwargs):
        self.my_id=str(self.request.get_full_path()).split('/')[1:2][0]
        return super().form_invalid(form)
        
    def form_valid(self,form):
        return super().form_valid(form)

class Delete_View(DeleteView):
    template_name='charges/delete.html'
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
        return get_object_or_404(Charges,cId=id_)