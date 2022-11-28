
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_seller = models.BooleanField(default=False,blank=True)
    gender = models.BooleanField(default=False, blank=True)
    birthday = models.DateField(auto_now_add=True, blank=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    account_no = models.CharField(max_length=100,blank=True,null=True)
    item_count = models.IntegerField(default=0, blank=True)
    avt = models.ImageField(upload_to='pictures/',max_length=255, null=True, blank=True)

class Seller(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)
    account_no = models.CharField(max_length=30, null=True, blank=True)
    name_store = models.CharField(max_length=100)
    facebook = models.URLField(max_length=256, blank=True, null=True)
    product_count = models.FloatField(default=0, blank=True)
    follower_count = models.IntegerField(default=0, blank=True)
    rating_average = models.FloatField(default=0, blank=True)
    response_rate = models.FloatField(default=0, blank=True)
    logo = models.ImageField(upload_to='pictures/',max_length=255)
    sku = models.CharField(max_length=256, null=True, blank=True)


