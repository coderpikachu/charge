from django.shortcuts import render, redirect ,get_object_or_404
from dormitory.forms import DormitoryForm  
from dormitory.models import Dormitory 
from flat.models import Flat 
from user.models import User 
from django.http import *
from django import forms 
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )
# Create your views here.  
class Create_View(CreateView):
    template_name='dormitory/index.html'
    form_class=DormitoryForm
    queryset=Dormitory.objects.all()
    success_url='../../dormitory/show/'
    my_id=''
    my_pwd=''
    request=None
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        self.my_pwd=kwargs['my_pwd']
        print(self.my_id)
        print(self.my_pwd)
        self.request=request
        #HttpRequest.POST({'my_id':self.my_id,'my_pwd':self.my_pwd})
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        print(self.my_id)
        print(self.my_pwd)
        context = super().get_context_data(**kwargs)
        #context['flat_objects']=Flat.objects.all().values()
        return context

    def form_valid(self,form,*args,**kwargs):
        print(0)
        print(self.request.get_full_path())
        print(str(self.request.get_full_path()))
        print(str(self.request.get_full_path()).split('/'))
        print(str(self.request.get_full_path()).split('/')[1:3])
        print(1)
        self.my_id,self.my_pwd=str(self.request.get_full_path()).split('/')[1:3]
        print(2)
        print(User.objects.filter(uId=self.my_id).values())
        print(3)
        t=User.objects.filter(uId=self.my_id).first().types
        print(t)
        if t=='C' and self.my_id != form.cleaned_data['dId']:
            raise forms.ValidationError('you can only create for you')
        return super().form_valid(form)

class List_View(ListView):
    template_name='dormitory/show.html'
    queryset=Dormitory.objects.all()

class Update_View(UpdateView):
    template_name='dormitory/edit.html'
    form_class=DormitoryForm
    queryset=Dormitory.objects.all()
    success_url='../../show/'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Dormitory,dId=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flat_objects']=Flat.objects.all().values()
        return context

    def form_valid(self,form):
        print(form.cleaned_data)
        print(Flat.objects.all().values())
        return super().form_valid(form)

class Delete_View(DeleteView):
    template_name='dormitory/delete.html'
    success_url='../../show/'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Dormitory,dId=id_)