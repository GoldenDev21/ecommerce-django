from rest_framework import viewsets
from .serializers import *
from .models import Brand, Color, Category, SubCategory, Product, Variant, PromoCode, Order, OrderItem


class BrandListView(generics.ListAPIView):
    """
    API endpoint that returns a list of brands.

    Accessible by all.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandCreateView(generics.ListCreateAPIView):
    """
    API endpoint that returns a list of brands & allows creation of a new brand.

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


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class PromoCodeViewSet(viewsets.ModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
