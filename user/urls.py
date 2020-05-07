from django.urls import path
from user import views
app_name='user'
urlpatterns=[
	path('u', views.u,name='u'),  
	path('show',views.show,name='show'),  
	path('edit/<int:id>', views.edit,name='edit'),  
	path('update/<int:id>', views.update,name='update'),  
	path('delete/<int:id>', views.destroy,name='delete'),
]