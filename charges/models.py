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
	cId=models.CharField(max_length=100,primary_key=True,unique=True)
	flatId=models.ForeignKey(Flat,to_field='fId',on_delete=models.CASCADE)
	dormitoryId=models.ForeignKey(Dormitory,to_field='dId',on_delete=models.CASCADE)
	chargeDate=models.DateField()
	
	money=models.DecimalField(decimal_places=2,max_digits=10)
	class Meta:  
		db_table = "charges"

	def __str__(self):
		return self.cId

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)