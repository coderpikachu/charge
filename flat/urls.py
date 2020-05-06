from django.urls import path
from flat import views
app_name='flat'
urlpatterns=[
	path('fl', views.fl,name='fl'),  
	path('show',views.show,name='show'),  
	path('edit/<int:id>', views.edit,name='edit'),  
	path('update/<int:id>', views.update,name='update'),  
	path('delete/<int:id>', views.destroy,name='delete'),
]