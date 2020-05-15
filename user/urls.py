from django.urls import path
from user.views import *
app_name='user'
urlpatterns=[
	path('create/', Create_View.as_view(),name='create'),  
	path('filterList/',filterListView,name='filterList'),  
	path('update/<int:id>/', Update_View.as_view(),name='update'),  
	path('delete/<int:id>/', Delete_View.as_view(),name='delete'),
]