from django.urls import path
from student.views import *
app_name='student'
urlpatterns=[
	path('create/', Create_View.as_view(),name='create'),  
	path('createOnly/', CreateOnly_View.as_view(),name='createOnly'),
	path('filterList/',filterListView,name='filterList'),  
	path('update/<int:id>/', Update_View.as_view(),name='update'),  
	path('delete/<int:id>/', Delete_View.as_view(),name='delete'),
]