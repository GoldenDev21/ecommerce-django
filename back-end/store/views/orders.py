from rest_framework import generics, permissions
from store.serializers import OrderSerializer
from store.models import Order


class OrderListCreateView(generics.ListAPIView):
    """
    View that returns a list of orders and allows creation of a new order.

    Accessible by authenticated users.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # TODO: Only allow users to view their own orders.


class OrderRetrieveEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the update or deletion of a single order.

    Accessible only by admin.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]


class OrderEditView(generics.RetrieveUpdateAPIView):
    """
    View that allows the retrieval and update of a single order.

    Accessible only by authenticated users.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]
    # TODO: Only allow users to edit their own orders, unless they are an admin.
