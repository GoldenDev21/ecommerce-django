from store.serializers import CategorySerializer
from store.models import Category
from rest_framework import generics, permissions


class CategoryDetailView(generics.RetrieveAPIView):
    """
    View that returns a detailed view of a single category.

    Accessible by all.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'url_key'
    permission_classes = [permissions.AllowAny]


class CategoryListView(generics.ListAPIView):
    """
    View that returns a list of all categories.

    Accessible by all.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]


class CategoryEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View that allows the update or deletion of a single category.

    Accessible only by admin.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]


class CategoryCreateView(generics.ListCreateAPIView):
    """
    Allows the creation of a category or lists all categories.

    Accessible only by admin.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]
