from .models import CustomUser, Profile
from rest_framework import generics, permissions
from .serializers import UserSerializer, ProfileSerializer


class UserListCreateView(generics.ListCreateAPIView):
    """
    View that returns a list of users and allows creation of a new user.

    Accessible by admin.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAdminUser]


class UserCreateView(generics.CreateAPIView):
    """
    View that allows creation of a new user.

    Accessible by all.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserRetrieveEditView(generics.RetrieveUpdateAPIView):
    """
    View that allows retrieval and edit of a user.

    Accessible by authenticated users.
    """
    queryset = CustomUser.objects.all()
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRetrieveEditDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows edit and deletion of a user.

    Accessible by admin.
    """
    queryset = CustomUser.objects.all()
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    View that allows view & edit of a profile.

    Accessible by authenticated users.
    """
    queryset = Profile.objects.all()
    lookup_field = 'pk'
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

