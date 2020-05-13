from django.db import models  
class Flat(models.Model): 	
	fId=models.CharField(max_length=100,primary_key=True,unique=True)
	layers=models.IntegerField()
	roomNum=models.IntegerField()
	openTime=models.TimeField()
	class Meta:  
		db_table = "flat"
	def __str__(self):
		return self.fId