from django.urls import path
from student import views
app_name='student'
urlpatterns=[
	path('st', views.StuCreateView.as_view(),name='st'),  
	path('show',views.StuListView.as_view(),name='show'),  
	path('edit/<int:id>/', views.StuUpdateView.as_view(),name='edit'),  
	path('delete/<int:id>/', views.StuDeleteView.as_view(),name='delete'),
]