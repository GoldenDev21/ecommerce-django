from .models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    """
    View that returns a list of users and allows creation of a new user.

    Accessible by admin.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]


class UserRetrieveEditDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows edit and deletion of a user.

    Accessible by admin.
    """
    queryset = User.objects.all()
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
