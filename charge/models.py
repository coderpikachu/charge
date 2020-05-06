from django.db import models  
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
	flatId=models.IntegerField()
	dormitoryId=models.IntegerField()
	chargeDate=models.DateField()
	
	money=models.DecimalField(decimal_places=2,max_digits=10)
	class Meta:  
		db_table = "charge"