from django.shortcuts import render
from rest_framework import Response, viewSets

from .models import Category
from .serializers import CategorySerializer

# Create your views here.

class CategoryView(viewSets.ViewSet):
    """
    This view returns all the Categories
    """
    def list(self,request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)