from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import authentication_classes, permission_classes
from serializers import EmployeeSerializers
from tasks.models import Employee
import json
# Create your views here.
@authentication_classes([])
@permission_classes([])
class EmployeeCreation(APIView):
	def post(self, request):
		try:
			print(request.data)
			cs = EmployeeSerializers(data = request.data)
			if cs.is_valid():
				res = cs.save()
				success_msg 	=	"Employee successfully created - %s"%res.id
				return Response(success_msg, status.HTTP_200_OK)
			else:
				return Response('Employee creation failed', status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err, status.HTTP_500_INTERNAL_SERVER_ERROR)

@authentication_classes([])
@permission_classes([])
class EmployeeDetails(APIView):
	def get(self, request):
		try:			
			emp = EmployeeSerializers(Employee.objects.all(), many=True)
			res = emp.data
			return Response(res, status.HTTP_200_OK)
		except Exception as err:
			return Response(err, status.HTTP_400_BAD_REQUEST)

@authentication_classes([])
@permission_classes([])
class EmployeeUpdation(APIView):
	def put(self, request, id):
		try:
			emp 	= Employee.objects.get(pk = id)
			srs 	= EmployeeSerializers(emp, data = request.data)
			if srs.is_valid():						
				srs.save()
				return Response('Employee Updated Successfully...', status.HTTP_200_OK)
			else:
				return Response('Employee Updation Failed', status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err, status.HTTP_500_INTERNAL_SERVER_ERROR)

@authentication_classes([])
@permission_classes([])
class EmployeeDeletion(APIView):
	def delete(self, request, id):
		try:
			c = Employee.objects.get(pk = id)
			c.delete()
			return Response('Employee deleted successfully...', status.HTTP_200_OK)
		except Exception as err:
			return Response(err, status.HTTP_500_INTERNAL_SERVER_ERROR)