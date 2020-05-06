from django.urls import path
from charge import views
app_name='charge'
urlpatterns=[
	path('ch', views.ch,name='ch'),  
	path('show',views.show,name='show'),  
	path('edit/<int:id>', views.edit,name='edit'),  
	path('update/<int:id>', views.update,name='update'),  
	path('delete/<int:id>', views.destroy,name='delete'),
]