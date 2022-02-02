from rest_framework import serializers

from accounts.serializers import ProfileSerializer
from .models import Brand, Color, Category, SubCategory, Product, Variant, PromoCode, Order, OrderItem


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


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'url_key', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    sub_category = SubCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'description', 'category', 'sub_category', 'url_key']


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
    profile = ProfileSerializer()
    discount_code = PromoCodeSerializer()

    class Meta:
        model = Order
        fields = ['id', 'profile', 'status', 'discount_code']


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    variant = VariantSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'variant', 'quantity']
