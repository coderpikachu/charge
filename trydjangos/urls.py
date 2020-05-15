from django.contrib import admin  
from django.urls import path,include
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', include('pages.urls')),
    path('<int:my_id>/student/',include('student.urls')),
    path('<int:my_id>/charges/',include('charges.urls')),
    path('<int:my_id>/flat/',include('flat.urls')),
    path('<int:my_id>/dormitory/',include('dormitory.urls')),
    path('<int:my_id>/user/',include('user.urls'))
]  