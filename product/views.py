from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    """
    This view returns all the Categories
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self,request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    This view returns all the Categories
    """
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self,request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class ProductViewSet(viewsets.ViewSet):
    """
    This view returns all the Categories
    """
    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self,request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)