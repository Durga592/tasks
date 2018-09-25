from rest_framework import serializers
from tasks.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
	class Meta:
		model 	=	Employee
		fields 	=	'__all__'