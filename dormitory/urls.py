from django.urls import path
from dormitory import views
app_name='dormitory'
urlpatterns=[
	path('dor/', views.Create_View.as_view(),name='dor'),  
	path('show/',views.List_View.as_view(),name='show'),  
	path('edit/<int:id>/', views.Update_View.as_view(),name='edit'),  
	path('delete/<int:id>/', views.Delete_View.as_view(),name='delete'),
]