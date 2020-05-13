from django.db import models  
from flat.models import Flat
class Dormitory(models.Model): 	
	dId=models.CharField(max_length=100,primary_key=True,unique=True)
	peopleNum=models.IntegerField()
	accommodationCharge=models.DecimalField(max_digits=10,decimal_places=2)
	telephone=models.CharField(max_length=100)
	flatId=models.ForeignKey(Flat,to_field='fId',on_delete=models.CASCADE)

	
	class Meta:  
		db_table = "dormitory"
	def __str__(self):
		return self.dId