from rest_framework import generics

from api.v1.serializers import ProductSerializer
from entities.product.models import Product

from rest_framework.permissions import IsAuthenticated


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
