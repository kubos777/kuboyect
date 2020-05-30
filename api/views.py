from django.shortcuts import render
from rest_framework import generics
from .models import Publication
from .serializers import PublicationSerializer

class PublicationList(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    
