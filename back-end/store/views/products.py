from store.serializers import ProductSerializer
from store.models import Product
from rest_framework import generics
from store.permissions import IsAdminOrReadOnly


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that returns a single product for unauthenticated or authenticated users.

    For admin, allows the update or deletion of a product.
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"
    permission_classes = [IsAdminOrReadOnly]


class ProductListCreateView(generics.ListCreateAPIView):
    """
    View that returns a list of all products for unauthenticated or authenticated users.

    For admin, allows creation of a new product.
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]
