from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
 class Meta:
  model = ProductCategory
  fields = ['categoryId','categoryName']

class ProductSerializer(serializers.ModelSerializer):
 category = CategorySerializer(many=False)
 class Meta:
  model = Product
  exclude = ('productWeight',)
  #fields = ['productName', 'category']

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields = ['username', 'password']
  extra_kwargs = {'password': {'write_only': True, 'required': True}}

 def create(self, validated_data):
  user = User.objects.create_user(**validated_data)
  Token.objects.create(user=user)
  return user

class OrdersSerializer(serializers.ModelSerializer):
 class Meta:
  model = Orders
  fields = '__all__'
  '''
  fields = ['orderId', 'user', 'orderAmount', 'orderShipName', 'orderShipAddress1', 'orderShipAddress2',
            'orderState', 'orderCity', 'orderZip', 'orderCountry', 'orderPhone', 'orderShippingAmount',
            'orderTax', 'orderEmail', 'orderDate', 'orderShipped', 'orderTrackingNumber']
  '''





