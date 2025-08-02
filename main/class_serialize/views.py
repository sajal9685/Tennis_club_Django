from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerilizers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class employees_view(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        serializer=EmployeeSerilizers(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=EmployeeSerilizers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response (serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)


class employees_detail(APIView):
    def get_object(self,pk):
        try:
            employee= Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        employee=self.get_object(pk)
        serializer= EmployeeSerilizers(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)    

    def put(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerilizers(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self ,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


