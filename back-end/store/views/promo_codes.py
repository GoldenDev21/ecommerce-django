from rest_framework import viewsets
from store.serializers import PromoCodeSerializer
from store.models import PromoCode


class PromoCodeViewSet(viewsets.ModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
