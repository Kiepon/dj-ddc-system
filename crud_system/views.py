from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import RecordCash
from .serializers import RecordCashSerializer


class RecordCashList(generics.ListCreateAPIView):
    queryset = RecordCash.objects.all()
    serializer_class = RecordCashSerializer
    
    

class RecordCashDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecordCash.objects.all()
    serializer_class = RecordCashSerializer
    
