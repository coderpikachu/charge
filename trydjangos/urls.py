from django.contrib import admin  
from django.urls import path,include
from pages.views import home_view,LogInView,signUp_view,logIn_view
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('logIn/', logIn_view),  
    path('signUp/', signUp_view), 
    path('home/', home_view),
    path('student/',include('student.urls')),
    path('charge/',include('charges.urls')),
    path('flat/',include('flat.urls')),
    path('dormitory/',include('dormitory.urls')),
    path('user/',include('user.urls'))
    # path('<int:my_id>/<int:my_pwd>/home', home_view),
    # path('<int:my_id>/<int:my_pwd>/student',include('student.urls')),
    # path('<int:my_id>/<int:my_pwd>/charge',include('charges.urls')),
    # path('<int:my_id>/<int:my_pwd>/flat',include('flat.urls')),
    # path('<int:my_id>/<int:my_pwd>/dormitory',include('dormitory.urls')),
    # path('<int:my_id>/<int:my_pwd>/user',include('user.urls'))
]  