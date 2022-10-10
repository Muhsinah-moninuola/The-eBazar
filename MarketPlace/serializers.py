from dataclasses import fields
from os import access
from rest_framework import serializers
from MarketPlace.models import *
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class GeneralRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length = 4)
    class Meta:
        model = User
        fields =['id','email', 'username','password'] 


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = userRegister
        fields =['id', 'phone_number'] 

class VendorRegisterSerializer(serializers.ModelSerializer):
    user = GeneralRegisterSerializer(required = True)
    class Meta:
        model = VendorRegister
        fields =['id','user', 'phone_number', 'business_name', 'business_logo', 'address'] 
