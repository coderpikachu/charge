from django.db import models  
class Dormitory(models.Model): 	
	dId=models.IntegerField()
	peopleNum=models.IntegerField()
	accommodationCharge=models.DecimalField(max_digits=10,decimal_places=2)
	telephone=models.IntegerField()
	flatId=models.IntegerField()

	
	class Meta:  
		db_table = "dormitory"