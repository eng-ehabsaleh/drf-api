from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers
from .serializer import SnackSerializer 
from .models import Snack

# Create your views here.
class SnackList(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer 

class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer 