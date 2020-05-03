from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone
import uuid

class ProductCategory(models.Model):
 categoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 categoryName = models.CharField(max_length=100, blank=False)

 def __str__(self):
  return self.categoryName

class Product(models.Model):
 productId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 productName = models.CharField(max_length=100, blank=False)
 productDescription = models.TextField(null=True)
 productPrice = models.DecimalField(blank=False, default=0.0, max_digits=5, decimal_places=2)
 productWeight = models.DecimalField(null=True, blank=False, max_digits=5, decimal_places=2)
 productImage = models.ImageField(upload_to='images/', blank=False)
 productCartDesc = models.TextField(null=True)
 productShortDesc = models.TextField(null=True)
 productUpdateDate = models.DateTimeField(default=timezone.now)
 productStock = models.IntegerField(default=0)
 productLiveStatus = models.BooleanField(default=False)
 productLocation = models.TextField(max_length=250, blank=True, null=True)
 category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=False, null=True)

 def __str__(self):
  return self.productName

class Orders(models.Model):
 orderId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 orderAmount = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
 orderShipName = models.CharField(blank=False, max_length=100)
 orderShipAddress1 = models.CharField(blank=False, max_length=100)
 orderShipAddress2 = models.CharField(blank=True, max_length=100, null=True)
 orderCity = models.CharField(blank=True, max_length=100, null=True)
 orderState = models.CharField(blank=True, max_length=100, null=True)
 orderZip = models.CharField(blank=True, max_length=100, null=True)
 orderCountry = models.CharField(blank=False, max_length=100)
 orderPhone = models.CharField(blank=False, max_length=100)
 orderShippingAmount = models.DecimalField(blank=False, max_digits=5, decimal_places=2, default=0.0)
 orderTax= models.DecimalField(blank=False, max_digits=5, decimal_places=2, default=0.0)
 orderEmail = models.CharField(blank=True, max_length=100, null=True)
 orderDate = models.DateTimeField(default=timezone.now)
 orderShipped = models.BooleanField(default=False)
 orderTrackingNumber = models.UUIDField(blank=False, default=uuid.uuid4, unique=True)

class OrderDetails(models.Model):
 detailId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 detailName = models.CharField(max_length=250, blank=False)
 detailPrice = models.DecimalField(null=True, blank=False, max_digits=5, decimal_places=2)
 detailQuantity = models.IntegerField(blank=False, default=0)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 detailOrderId = models.ForeignKey(Orders, on_delete=models.CASCADE)

 def __str__(self):
  return self.detailName

