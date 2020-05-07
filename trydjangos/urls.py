from django.contrib import admin  
from django.urls import path,include
from pages.views import home_view,logIn_view,signUp_view
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', logIn_view),  
    path('signUp', signUp_view), 
    path('<int:id>/<int:pwd>/home', home_view),
    path('<int:id>/<int:pwd>/student',include('student.urls')),
    path('<int:id>/<int:pwd>/charge',include('charge.urls')),
    path('<int:id>/<int:pwd>/flat',include('flat.urls')),
    path('<int:id>/<int:pwd>/dormitory',include('dormitory.urls')),
    path('<int:id>/<int:pwd>/user',include('user.urls'))
]  