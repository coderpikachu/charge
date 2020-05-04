from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)
def article_detail_view(request,*args,**kwargs):
	context={}
	return render(request,'blog/article_detail.html',context)

def article_list_view(request,*args,**kwargs):
	form=ArticleForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ArticleForm(request.POST or None)
	context={
	"form":form
	}
	return render(request,'blog/article_list.html',context)

class ArticleListView(ListView):
	queryset=Article.objects.all()