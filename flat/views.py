from django.shortcuts import render, redirect,get_object_or_404
from flat.forms import FlatForm  
from flat.models import Flat  
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
    )
class Create_View(CreateView):
    template_name='flat/index.html'
    form_class=FlatForm
    queryset=Flat.objects.all()
    success_url='../../flat/show/'
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class List_View(ListView):
    template_name='flat/show.html'
    queryset=Flat.objects.all()

class Update_View(UpdateView):
    template_name='flat/edit.html'
    form_class=FlatForm
    queryset=Flat.objects.all()
    success_url='../../show'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Flat,fId=id_)
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class Delete_View(DeleteView):
    template_name='flat/delete.html'
    success_url='../../show'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Flat,sId=id_)