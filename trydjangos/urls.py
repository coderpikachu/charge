from django.contrib import admin  
from django.urls import path,include
from pages.views import home_view
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', home_view),   
    path('student/',include('student.urls')),
    path('charge/',include('charge.urls')),
    path('flat/',include('flat.urls')),
    path('dormitory/',include('dormitory.urls'))
]  