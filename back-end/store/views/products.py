from store.serializers import ProductSerializer, VariantSerializer
from store.models import Product, Variant
from rest_framework import generics, permissions


class ProductDetailView(generics.RetrieveAPIView):
    """
    View that returns a single product.

    Accessible by all.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.AllowAny]


class ProductListView(generics.ListAPIView):
    """
    View that returns a list of all products.

    Accessible by all.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]


class ProductEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the update or deletion of a single product.

    Accessible only by admin.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]


class ProductCreateView(generics.ListCreateAPIView):
    """
    Allows the creation of a product or lists all products.

    Accessible only by admin.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]


class VariantListView(generics.ListAPIView):
    """
    View that returns a list of all variants.

    Accessible by all.
    """
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()
    permission_classes = [permissions.AllowAny]


class VariantEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the update or deletion of a single variant.

    Accessible only by admin.
    """
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]


class VariantCreateView(generics.ListCreateAPIView):
    """
    Allows the creation of a product or lists all variants.

    Accessible only by admin.
    """
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()
    permission_classes = [permissions.IsAdminUser]
