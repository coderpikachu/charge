from django.db import models  
class Flat(models.Model): 	
	fId=models.IntegerField()
	layers=models.IntegerField()
	roomNum=models.IntegerField()
	openTime=models.DateField()
	class Meta:  
		db_table = "flat"