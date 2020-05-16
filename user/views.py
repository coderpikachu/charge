from django.shortcuts import render, redirect ,get_object_or_404
from user.forms import UserForm  
from user.models import User 
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
from .filters import UserFilter
# Create your views here.  
class Create_View(CreateView):
    template_name='user/create.html'
    form_class=UserForm
    queryset=User.objects.all()
    success_url='../../user/filterList/'
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

def filterListView(request,*args,**kwargs):
    authority=User.objects.filter(uId=kwargs['my_id']).first()
    user_add=authority.user_add
    user_edit=authority.user_edit
    user_delete=authority.user_delete
    filter = UserFilter(request.GET, queryset=User.objects.all())
    return render(request, 'user/filterList.html', {'filter': filter,'my_id':kwargs['my_id'],'user_add':user_add,
        'user_edit':user_edit,'user_delete':user_delete})

class Update_View(UpdateView):
    template_name='user/update.html'
    form_class=UserForm
    queryset=User.objects.all()
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
        return get_object_or_404(User,uId=id_)

    def form_invalid(self,form,*args,**kwargs):
        self.my_id=str(self.request.get_full_path()).split('/')[1:2][0]
        return super().form_invalid(form)

    def form_valid(self,form):
        return super().form_valid(form)

class Delete_View(DeleteView):
    template_name='user/delete.html'
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
        return get_object_or_404(User,uId=id_)