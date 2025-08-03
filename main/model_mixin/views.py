from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins
from .serializers import TeacherSerializer
from .models import Teachers
from rest_framework import generics

# Create your views here.
class teachers_view(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeacherSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)


class teachers_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeacherSerializer

    def get (self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
