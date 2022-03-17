from store.serializers import BrandSerializer
from store.models import Brand
from rest_framework import generics
from store.permissions import IsAdminOrReadOnly


class BrandListCreateView(generics.ListCreateAPIView):
    """
    View that returns a list of all brands for unauthenticated or authenticated users.

    For admin, allows creation of a new brand.
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class BrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that returns a single brand for unauthenticated or authenticated users.

    For admin, allows the update or deletion of a brand.
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]
