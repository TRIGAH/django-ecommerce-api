from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category
from .serializers import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    """
    This view returns all the Categories
    """
    queryset = Category.objects.all()

    @extend_schema(resposes=CategorySerializer)
    def list(self,request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)