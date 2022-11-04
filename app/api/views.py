from app.models import User
from app.api.serializers import CustomerSerializer,ProductSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.models import Customer,Product
# from myshop.app.models import Product

class CustomerViewSet(viewsets.ModelViewSet):
 queryset = Customer.objects.all()
 serializer_class = CustomerSerializer
 authentication_classes = [SessionAuthentication]
 permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer
 authentication_classes = [SessionAuthentication]
 permission_classes = [IsAuthenticatedOrReadOnly]