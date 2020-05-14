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
    template_name='dormitory/index.html'
    form_class=DormitoryForm
    queryset=Dormitory.objects.all()
    success_url='../../dormitory/show/'
    my_id=''
    my_pwd=''
    request=None
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        print(self.my_id)
        self.request=request
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        print('00')
        print(self.my_id)
        print(11)
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
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        self.request=request
        return super().get(self,request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        print(self.request.POST.get('dId'))
        dId=self.request.POST.get('dId') if self.request.POST.get('dId')!=None else ""
        peopleNum=self.request.POST.get('peopleNum') if self.request.POST.get('peopleNum')!=None else None
        accommodationCharge=self.request.POST.get('accommodationCharge') if self.request.POST.get('accommodationCharge')!=None else None
        telephone=self.request.POST.get('telephone') if self.request.POST.get('telephone')!=None else ""
        flatId=self.request.POST.get('flatId') if self.request.POST.get('flatId')!=None else None
        self.queryset=Dormitory.objects.filter(
            dId__contains=dId,
            peopleNum=peopleNum,
            accommodationCharge=accommodationCharge,
            telephone__contains=telephone,
            flatId__contains=flatId,
            )
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        return context

def dormitory_list(request,*args,**kwargs):
    filter = DormitoryFilter(request.GET, queryset=Dormitory.objects.all())
    return render(request, 'dormitory/show.html', {'filter': filter,'my_id':kwargs['my_id']})

class DormitoryList(FilterView):
    model = Dormitory
    template_name = 'dormitory/show.html'
    context_object_name = 'dormitories'
    filterset_class = DormitoryFilter
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        print(self.my_id)
        self.request=request
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        print('00')
        print(self.my_id)
        print(11)
        return context

class Update_View(UpdateView):
    template_name='dormitory/edit.html'
    form_class=DormitoryForm
    queryset=Dormitory.objects.all()
    success_url='../../show/'
    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        print(self.my_id)
        self.request=request
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        print('00')
        print(self.my_id)
        print(11)
        return context
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Dormitory,dId=id_)

    def form_valid(self,form):
        print(form.cleaned_data)
        print(Flat.objects.all().values())
        return super().form_valid(form)

class Delete_View(DeleteView):
    template_name='dormitory/delete.html'
    success_url='../../show/'

    def get(self, request, *args, **kwargs):
        self.my_id=kwargs['my_id']
        print(self.my_id)
        self.request=request
        return super().get(self,request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_id']=self.my_id
        print('00')
        print(self.my_id)
        print(11)
        return context
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Dormitory,dId=id_)