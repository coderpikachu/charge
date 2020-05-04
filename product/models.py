from django.db import models

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=10)
	description=models.TextField(null=True,blank=True)
	price =models.DecimalField(max_digits=10,decimal_places=2)
		