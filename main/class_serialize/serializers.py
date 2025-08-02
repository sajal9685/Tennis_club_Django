from rest_framework import serializers
from class_serialize.models import Employee

class EmployeeSerilizers(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields="__all__"    
