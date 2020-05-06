from django.db import models  
from flat.models import Flat
from dormitory.models import Dormitory
class Charge(models.Model): 	
	Water='W'
	Food='F'
	Electricity='E'
	Accommodation='A'
	chargeChoices=[	
		(Water,'Water'),
		(Food,'Food'),
		(Electricity,'Electricity'),
		(Accommodation,'Accommodation')
	]
	chargeType=models.CharField(
		max_length=4,
		choices=chargeChoices,
		default=Water,
    )
	cId=models.IntegerField()
	flatId=models.ForeignKey(Flat,on_delete=models.CASCADE)
	dormitoryId=models.ForeignKey(Dormitory,on_delete=models.CASCADE)
	chargeDate=models.DateField()
	
	money=models.DecimalField(decimal_places=2,max_digits=10)
	class Meta:  
		db_table = "charge"