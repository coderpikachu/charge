from django.urls import path
from dormitory import views
app_name='dormitory'
urlpatterns=[
	path('dor', views.dor,name='dor'),  
	path('show',views.show,name='show'),  
	path('edit/<int:id>', views.edit,name='edit'),  
	path('update/<int:id>', views.update,name='update'),  
	path('delete/<int:id>', views.destroy,name='delete'),
]