from dormitory.models import Dormitory
from django.db import models  
from student.models import Student
class User(models.Model): 	
	Super='S'
	Admin='F'
	Common='C'
	userChoices=[	
		(Super,'S'),
		(Admin,'A'),
		(Common,'C'),
	]
	uId=models.OneToOneField(
		Student,
		on_delete=models.CASCADE
		)
	name=models.CharField(max_length=100)
	pwd=models.CharField(max_length=100)
	types=models.CharField(
		max_length=2,
		choices=userChoices,
		default=Common,
		)
	# authority=[
	# 'student':[
	# 	'search':True,
	# 	'add':True,
	# 	'modify'
	# ]
	# ]
	class Meta:  
		db_table = "user"