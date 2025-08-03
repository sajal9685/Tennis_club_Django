from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets 
from rest_framework.response import Response
from func_serialize.models import Students
from func_serialize.serializers import StudentSerializers
# Create your views here.
'''
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Students.objects.all()
        serializer = StudentSerializers(queryset , many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        student=get_object_or_404(Students,pk=pk)
        serializer=StudentSerializers(student)
        return Response(serializer.data)
    Same for - create , retrieve, update and delete in same class
'''

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=StudentSerializers