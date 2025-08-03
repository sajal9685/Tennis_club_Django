from django.shortcuts import render
from rest_framework import generics
from .models import Family
from .serializers import FamilySerializer

# Create your views here.
"""
class family_view(generics.ListAPIView,generics.CreateAPIView):
    queryset=Family.objects.all()
    serializer_class=FamilySerializer



class family_detail(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Family.objects.all()
    serializer_class=FamilySerializer
    lookup_field="pk"
"""


class family_view(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class family_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    lookup_field = "pk"
