from dormitory.models import Dormitory
from django.db import models  
class LogIn(models.Model): 	
	uId=models.CharField(
		max_length=100
		)
	pwd=models.CharField(max_length=100)
	class Meta:  
		db_table = "pages"