from django.db import models  
from flat.models import Flat
from dormitory.models import Dormitory
class Charges(models.Model): 	
	Water='W'
	Food='F'
	Electricity='E'
	Accommodation='A'
	Trash='T'
	chargeChoices=[	
		(Water,'Water'),
		(Food,'Food'),
		(Electricity,'Electricity'),
		(Accommodation,'Accommodation'),
		(Trash,'Trash')
	]
	chargeType=models.CharField(
		max_length=4,
		choices=chargeChoices,
		default=Water,
    )
	cId=models.CharField(max_length=100,primary_key=True)
	flatId=models.ForeignKey(Flat,on_delete=models.CASCADE)
	dormitoryId=models.ForeignKey(Dormitory,on_delete=models.CASCADE)
	chargeDate=models.DateField()
	
	money=models.DecimalField(decimal_places=2,max_digits=10)
	class Meta:  
		db_table = "charges"