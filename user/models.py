from dormitory.models import Dormitory
from django.db import models  
class User(models.Model): 	
	Super='S'
	Admin='A'
	Common='C'
	userChoices=[	
		(Super,'Super'),
		(Admin,'Admin'),
		(Common,'Common'),
	]
	uId=models.CharField(
		max_length=100,
		)
	name=models.CharField(max_length=100)
	pwd=models.CharField(max_length=100)
	types=models.CharField(
		max_length=3,
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