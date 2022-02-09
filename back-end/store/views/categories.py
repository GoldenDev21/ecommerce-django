from rest_framework import generics
from store.serializers import BrandSerializer, CategorySerializer
from store.models import Brand, Category


class CategoryListView(generics.ListAPIView):
    """
    API endpoint that returns a list of categories.

    Accessible by all.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryCreateView(generics.CreateAPIView):
    """
    API endpoint that allows creation of a new category.

    Accessible only by store managers.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryEditView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that returns a category & allows editing or deleting that category.

    Accessible only by store managers.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
