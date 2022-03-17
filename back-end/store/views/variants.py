from store.serializers import VariantReadOnlySerializer
from store.models import  Variant
from rest_framework import generics, permissions


class VariantEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the edit or deletion of a single variant.
    All fields are read-only except for qty_in_stock and image.

    Accessible only by admin.
    """
    serializer_class = VariantReadOnlySerializer
    queryset = Variant.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]
