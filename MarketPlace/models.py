from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class User(AbstractUser):
    is_buyer = models.BooleanField(default =False)
    is_vendor = models.BooleanField(default =False)
    
class userRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    phone_number = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)

    
class VendorRegister(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    business_name = models.CharField(max_length = 100)
    address = models.TextField()
    phone_number = models.CharField(max_length = 20)
    business_logo = models.ImageField(upload_to = "logo/", null=True, blank=True)
    approval = models.BooleanField(default=False)

class ProductCategory(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)

class product(models.Model):
    STATUS_TYPE = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish')
    )
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="productimage/", null=True, blank=True)
    Productcategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_TYPE)
    approval = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    Review = models.TextField(max_length=2000)
    name = models.CharField(max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)










