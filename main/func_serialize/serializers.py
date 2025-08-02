from rest_framework import serializers
from func_serialize.models import Students
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model= Students
        fields="__all__"
