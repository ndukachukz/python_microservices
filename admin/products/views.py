from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Product
from .serializers import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self,request): # /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)

    
    def create(self,request): # /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk:None): # /api/products/<str:id>
        pass

    def update(self,request, pk:None): # /api/products/<str:id>
        pass

    def destroy(self,request, pk:None): # /api/products/<str:id>
        pass