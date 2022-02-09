from rest_framework import generics
from store.serializers import BrandSerializer, ProductSerializer
from store.models import Brand, Product


class BrandListView(generics.ListAPIView):
    """
    API endpoint that returns a list of brands.

    Accessible by all.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandCreateView(generics.CreateAPIView):
    """
    API endpoint that allows creation of a new brand.

    Accessible only by store managers.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BrandEditView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that returns a brand & allows editing or deleting that brand.

    Accessible only by store managers.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
