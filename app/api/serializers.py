from app.models import Customer , Product
from rest_framework import serializers

# from myshop.app.models import Product

class CustomerSerializer(serializers.ModelSerializer):
 class Meta:
  model = Customer
  fields = ['id', 'user','name', 'locality', 'city','zipcode', 'state']


class ProductSerializer(serializers.ModelSerializer):
 class Meta:
  model = Product
  fields = ['id', 'title','selling_price', 'discounted_price', 'description','brand', 'category', 'product_image']  