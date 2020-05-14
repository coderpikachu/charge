from django.contrib import admin  
from django.urls import path,include
from pages.views import home_view,LogInView,signUp_view,logIn_view
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', logIn_view),  
    path('signUp/', signUp_view), 
    path('<int:my_id>/home/', home_view),
    path('<int:my_id>/student/',include('student.urls')),
    path('<int:my_id>/charge/',include('charges.urls')),
    path('<int:my_id>/flat/',include('flat.urls')),
    path('<int:my_id>/dormitory/',include('dormitory.urls')),
    path('<int:my_id>/user/',include('user.urls'))
]  