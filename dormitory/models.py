from django.db import models  
from flat.models import Flat
class Dormitory(models.Model): 	
	dId=models.IntegerField()
	peopleNum=models.IntegerField()
	accommodationCharge=models.DecimalField(max_digits=10,decimal_places=2)
	telephone=models.IntegerField()
	flatId=models.ForeignKey(Flat,on_delete=models.CASCADE)

	
	class Meta:  
		db_table = "dormitory"