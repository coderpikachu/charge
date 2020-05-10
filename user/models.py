from dormitory.models import Dormitory
from django.db.models import *
from django_mysql.models import JSONField
class User(Model): 	
	Super='S'
	Admin='A'
	Common='C'
	userChoices=[	
		(Super,'Super'),
		(Admin,'Admin'),
		(Common,'Common'),
	]
	uId=CharField(
		primary_key=True,
		max_length=100,
		)
	name=CharField(max_length=100)
	pwd=CharField(max_length=100)
	types=CharField(
		max_length=3,
		choices=userChoices,
		default=Common,
		)
	# authority=JSONField()
	student_add=BooleanField(default=True)
	student_edit=BooleanField(default=True)
	student_delete=BooleanField(default=True)

	flat_add=BooleanField(default=True)
	flat_edit=BooleanField(default=True)
	flat_delete=BooleanField(default=True)

	dormitory_add=BooleanField(default=True)
	dormitory_edit=BooleanField(default=True)
	dormitory_delete=BooleanField(default=True)

	charge_add=BooleanField(default=True)
	charge_edit=BooleanField(default=True)
	charge_delete=BooleanField(default=True)

	user_add=BooleanField(default=True)
	user_edit=BooleanField(default=True)
	user_delete=BooleanField(default=True)
	class Meta:  
		db_table = "user"