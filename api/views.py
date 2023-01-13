from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ecom.models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["name", "category__name"]
