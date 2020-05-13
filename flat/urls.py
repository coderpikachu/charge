from django.urls import path
from flat import views
app_name='flat'
urlpatterns=[
	path('fl',views.Create_View.as_view(),name='fl'),  
	path('show',views.List_View.as_view(),name='show'),  
	path('edit/<int:id>/', views.Update_View.as_view(),name='edit'),  
	path('delete/<int:id>/', views.Delete_View.as_view(),name='delete'),
]