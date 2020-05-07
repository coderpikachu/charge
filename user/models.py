from dormitory.models import Dormitory
from django.db import models  
class User(models.Model): 	
	Male='M'
	Female='F'
	genderChoices=[	
		(Male,'Male'),
		(Female,'Female'),
	]

	sId = models.CharField(max_length=20)
	name = models.CharField(max_length=100)
	gender=models.CharField(
		max_length=2,
		choices=genderChoices,
		default=Male,
    )
	nation=models.CharField(max_length=100)
	specialty=models.CharField(max_length=100)
	classId=models.IntegerField()
	telephone=models.CharField(max_length=100)
	flatId=models.ForeignKey(Flat,on_delete=models.CASCADE)
	dormitoryId=models.ForeignKey(Dormitory,on_delete=models.CASCADE)
	class Meta:  
		db_table = "student"