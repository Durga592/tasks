from django.db import models

# Create your models here.
class Employee(models.Model):
	first_name		=	models.CharField(max_length=250)
	last_name		=	models.CharField(max_length=250)
	device_id		=	models.IntegerField()
	class Meta:
		db_table	=	'employee'