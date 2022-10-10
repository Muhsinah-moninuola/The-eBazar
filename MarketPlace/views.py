from django.shortcuts import render
from unicodedata import category
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from MarketPlace.models import *
from MarketPlace.serializers import *
from django.contrib.auth.hashers import make_password

# Create your views here.
class UserRegistrationAPIView(generics.ListCreateAPIView):
    queryset = userRegister.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save(password = make_password(data['password']))

class VendorRegistrationAPIView(generics.ListCreateAPIView):
    queryset = VendorRegister.objects.filter(approval=True)
    serializer_class = VendorRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save(password = make_password(data['password']))


    
