from rest_framework import viewsets, status
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer

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
    return Response("The status param " + _status + " wasn't found ", status=status.HTTP_200_OK)
  else:
    return Response("You need to specify a status param for your search", status=status.HTTP_400_BAD_REQUEST)
