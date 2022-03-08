from rest_framework import serializers

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


class VariantSerializer(serializers.ModelSerializer):
    color = ColorSerializer()

    class Meta:
        model = Variant
        fields = ['id', 'sku', 'qty_in_stock', 'color', 'size', 'image']


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'description', 'category', 'url_key', 'variants']

    def create(self, validated_data):
        variants = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)
        for variant in variants:
            Variant.objects.create(product=product, **variant)
        return product


class PromoCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PromoCode
        fields = ['id', 'active', 'code', 'discount_percent', 'type']


class OrderItemSerializer(serializers.ModelSerializer):
    variant = VariantSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'variant', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    discount_code = PromoCodeSerializer()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'discount_code', 'items']



