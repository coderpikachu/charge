from django.urls import path
from student import views
app_name='student'
urlpatterns=[
	path('st', views.st,name='st'),  
	path('show',views.show,name='show'),  
	path('edit/<int:id>', views.edit,name='edit'),  
	path('update/<int:id>', views.update,name='update'),  
	path('delete/<int:id>', views.destroy,name='delete'),
]