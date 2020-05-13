from flat.models import Flat
from dormitory.models import Dormitory
from django.db import models  
from user.models import User
class Student(models.Model): 	
	Male='M'
	Female='F'
	genderChoices=[	
		(Male,'Male'),
		(Female,'Female'),
	]

	sId = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,unique=True)
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
	flatId=models.ForeignKey(Flat,to_field='fId',on_delete=models.CASCADE)
	dormitoryId=models.ForeignKey(Dormitory,to_field='dId',on_delete=models.CASCADE)
	class Meta:  
		db_table = "student"
	def __str__(self):
		return self.sId