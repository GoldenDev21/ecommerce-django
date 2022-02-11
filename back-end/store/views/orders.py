from rest_framework import viewsets, generics
from store.serializers import OrderSerializer, OrderItemSerializer
from store.models import Order, OrderItem


class OrderListView(generics.ListAPIView):
    """
    View that returns a list of orders.

    Accessible by all.
    """

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
