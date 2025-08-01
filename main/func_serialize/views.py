from django.shortcuts import render
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Students


# Create your views here.
@api_view(["GET","POST"])
def students_view(request):
    if request.method == "GET":
        students = Students.objects.all()
        serializers = StudentSerializers(students, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(["GET","PUT","DELETE"])
def students_detail(request,pk):
    try:
        students=Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    if request.method=="GET":
        serializer=StudentSerializers(students)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    elif request.method=="PUT":
        serializer=StudentSerializers(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method =="DELETE":
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    