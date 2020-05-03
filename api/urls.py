from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrdersViewSet)
router.register('users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]