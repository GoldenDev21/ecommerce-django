from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Brand, Color, Category, Product, Variant, PromoCode, Order, OrderItem


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'abbreviation']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'abbreviation', 'password']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'url_key', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'description', 'category', 'url_key']


class VariantSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    product = ProductSerializer()

    class Meta:
        model = Variant
        fields = ['id', 'sku', 'qty_in_stock', 'color', 'size', 'image', 'product']


class PromoCodeSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    product = ProductSerializer()

    class Meta:
        model = PromoCode
        fields = ['id', 'active', 'code', 'discount_percent', 'type']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    discount_code = PromoCodeSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'discount_code']


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    variant = VariantSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'variant', 'quantity']
