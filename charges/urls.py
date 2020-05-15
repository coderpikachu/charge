from django.urls import path
from charges.views import *
app_name='charges'
urlpatterns=[
	path('create/', Create_View.as_view(),name='create'),  
	path('filterList/',filterListView,name='filterList'),  
	path('update/<int:id>/', Update_View.as_view(),name='update'),  
	path('delete/<int:id>/', Delete_View.as_view(),name='delete'),
]