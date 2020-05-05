from django.db import models  
class Student(models.Model): 	
	Male='M'
	Female='F'
	genderChoices=[	
		(Male,'Male'),
		(Female,'Female'),
	]

	sid = models.CharField(max_length=20)
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
	flatId=models.IntegerField()
	dormitoryId=models.IntegerField()
	class Meta:  
		db_table = "student"