from rest_framework import serializers
from .models import *

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