from .models import User, Address
from rest_framework import generics, permissions
from .serializers import UserSerializer, AddressSerializer
from store.permissions import IsOwnerOrAdmin


class UserListCreateView(generics.ListCreateAPIView):
    """
    View that returns a list of users and allows creation of a new user.

    Accessible by admin.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]


class UserCreateView(generics.CreateAPIView):
    """
    View that allows an anonymous user to create an account.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserRetrieveEditDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows edit and deletion of a user.

    Accessible by admin.
    """
    queryset = User.objects.all()
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows edit and deletion of an address.

    Accessible by authenticated users if they are the user associated with the address
    or an admin.
    """
    queryset = Address.objects.all()
    lookup_field = 'pk'
    serializer_class = AddressSerializer
    permission_classes = [IsOwnerOrAdmin]


class AddressListView(generics.ListCreateAPIView):
    """
    View that allows returns a list of all addresses and allows the creation of a new one.

    Accessible by authenticated users.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
