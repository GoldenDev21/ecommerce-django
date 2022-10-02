from accounts.models import User, Address
from accounts.serializers import UserSerializer, AddressSerializer, CurrentUserSerializer
from django.contrib.auth import login
from store.permissions import IsOwnerOrAdmin
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from knox.views import LoginView as KnoxLoginView


class LoginView(KnoxLoginView):
    permission_classes = [AllowAny,]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserListCreateView(ListCreateAPIView):
    """
    View that returns a list of users and allows creation of a new user.

    Accessible by admin.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserCreateView(CreateAPIView):
    """
    View that allows an anonymous user to create an account.
    """

    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CurrentUserView(RetrieveAPIView):
    """
    View that returns the current user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CurrentUserSerializer

    def get_object(self):
        return self.request.user


class UserRetrieveEditDestroyView(RetrieveUpdateDestroyAPIView):
    """
    View that allows edit and deletion of a user.

    Accessible by admin.
    """

    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class AddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    View that allows edit and deletion of an address.

    Accessible by authenticated users if they are the user associated with the address
    or an admin.
    """

    queryset = Address.objects.all()
    lookup_field = "pk"
    serializer_class = AddressSerializer
    permission_classes = [IsOwnerOrAdmin]


class AddressListView(ListCreateAPIView):
    """
    View that allows returns a list of all addresses and allows the creation of a new one.

    Accessible by authenticated users.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
