from rest_framework import generics, permissions
from store.serializers import OrderSerializer
from store.models import Order
from store.permissions import IsOwnerOrAdmin


class OrderListCreateView(generics.ListCreateAPIView):
    """
    View that returns a list of orders and allows creation of a new order.

    Accessible by authenticated users.
    """
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Will return a list of all purchases for the currently authenticated
        user. Otherwise, if the user is an admin, will return all.
        :return:
        """
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)


class OrderRetrieveEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the update or deletion of a single order.

    Accessible only by the owner of the order or an admin.
    """
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        """
        Will return a list of all purchases for the currently authenticated
        user. Otherwise, if the user is an admin, will return all.
        :return:
        """
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)
