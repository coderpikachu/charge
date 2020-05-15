from django.urls import path
from pages.views import *
app_name='pages'
urlpatterns=[
	path('', logInView),  
    path('signUp/', signUpView), 
    path('<int:my_id>/home/', homeView),
]