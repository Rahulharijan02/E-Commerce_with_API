from django.urls import path, include
from app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customer', views.CustomerViewSet, basename='Customer')
router.register('product', views.ProductViewSet, basename='Product')

urlpatterns = [
    path('', include(router.urls))
]
