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
	student_add=BooleanField()
	student_edit=BooleanField()
	student_delete=BooleanField()

	flat_add=BooleanField()
	flat_edit=BooleanField()
	flat_delete=BooleanField()

	dormitory_add=BooleanField()
	dormitory_edit=BooleanField()
	dormitory_delete=BooleanField()

	charge_add=BooleanField()
	charge_edit=BooleanField()
	charge_delete=BooleanField()

	user_add=BooleanField()
	user_edit=BooleanField()
	user_delete=BooleanField()
	class Meta:
		db_table = "user"
	def __str__(self):
		return	self.uId