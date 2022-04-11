from store.serializers import CategorySerializer
from store.models import Category
from rest_framework import generics
from store.permissions import IsAdminOrReadOnly


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that returns a single category for unauthenticated or authenticated users.

    For admin, allows the update or deletion of a category.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "pk"
    permission_classes = [IsAdminOrReadOnly]


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    View that returns a list of all categories for unauthenticated or authenticated users.

    For admin, allows creation of a new category.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]
