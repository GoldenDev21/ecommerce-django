from store.serializers import BrandSerializer
from store.models import Brand
from rest_framework import generics, permissions


class BrandListView(generics.ListAPIView):
    """
   View that returns a list of all brands.

   Accessible by all.
   """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [permissions.AllowAny]


class BrandEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the update or deletion of a single brand.

    Accessible only by admin.
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    # permission_classes = [permissions.IsAdminUser]


class BrandCreateView(generics.ListCreateAPIView):
    """
    Allows the creation of a brand or lists all brands.

    Accessible only by admin.
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    # permission_classes = [permissions.IsAdminUser]


class BrandDetailView(generics.RetrieveAPIView):
    """
    View that returns a single brand.

    Accessible by all.
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    lookup_field = 'pk'
