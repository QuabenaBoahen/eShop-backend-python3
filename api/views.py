from rest_framework import viewsets, status
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer
 #authentication_classes = (TokenAuthentication,)
 permission_classes = (AllowAny,)

 @action(detail=False, methods=['GET'], url_path='specific-products')
 def getSpecificProductsBasedOnParams(self, request):
  #status: status/category param of product i.e Featured, New Arrival, etc
  queryset = Product.objects.all()
  _status = request.query_params.get('status', None)
  if _status is not None:
   try:
    category = ProductCategory.objects.get(categoryName=_status)
    queryset = queryset.filter(category=category.categoryId).values()
    return Response(queryset)
   except ProductCategory.DoesNotExist:
    return Response("The status param " + _status + " wasn't found ", status=status.HTTP_404_NOT_FOUND)
  else:
    return Response("You need to specify a status param for your search", status=status.HTTP_400_BAD_REQUEST)

class OrdersViewSet(viewsets.ModelViewSet):
 queryset = Orders.objects.all()
 serializer_class = OrdersSerializer
 authentication_classes = (TokenAuthentication,)
 permission_classes = (IsAuthenticated,)

 def create(self, request, *args, **kwargs):
  if not request.data.get('orderAmount', None):
   response = {"message": "orderAmount field is required", "status": 400}
   return Response(response, status=status.HTTP_400_BAD_REQUEST)
  elif not request.data.get('orderShipName', None):
   response = {"message": "orderShipName field is required", "status": 400}
   return Response(response, status=status.HTTP_400_BAD_REQUEST)
  elif not request.data.get('orderShipAddress1', None):
   response = {"message": "orderShipAddress1 field is required", "status": 400}
   return Response(response, status=status.HTTP_400_BAD_REQUEST)
  elif not request.data.get('orderPhone', None):
   response = {"message": "orderPhone field is required", "status": 400}
   return Response(response, status=status.HTTP_400_BAD_REQUEST)
  elif not request.data.get('orderCountry', None):
   response = {"message": "orderCountry field is required", "status": 400}
   return Response(response, status=status.HTTP_400_BAD_REQUEST)
  elif not request.data.get('orderCountry', None):
   response = {"message": "orderCountry field is required", "status": 400}
   return Response(response, status=status.HTTP_400_BAD_REQUEST)
  else:
   request.data['user'] = request.user.id
   request.data['orderEmail'] = request.user.email
   serializer = self.get_serializer(data=request.data)
   serializer.is_valid(raise_exception=True)
   self.perform_create(serializer)
   headers = self.get_success_headers(serializer.data)
   response = {"message": "Order saved successfully ", "result": serializer.data, "status": 201}
   return Response(response, status=status.HTTP_201_CREATED, headers=headers)

class UsersViewSet(viewsets.ModelViewSet):
 queryset = User.objects.all()
 serializer_class = UserSerializer

 #authentication_classes = (TokenAuthentication,)
 permission_classes = (AllowAny,)





