from store.serializers import PromoCodeSerializer
from store.models import PromoCode
from rest_framework import generics, permissions


class PromoCodeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the update or deletion of a single promo code.

    Accessible only by admin.
    """
    serializer_class = PromoCodeSerializer
    queryset = PromoCode.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]


class PromoCodeListCreateView(generics.ListCreateAPIView):
    """
    Allows the creation of a promo code or lists all promo codes.

    Accessible only by admin.
    """
    serializer_class = PromoCodeSerializer
    queryset = PromoCode.objects.all()
    permission_classes = [permissions.IsAdminUser]
