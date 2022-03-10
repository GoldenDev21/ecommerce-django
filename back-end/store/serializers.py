from rest_framework import serializers

from .models import Brand, Category, Product, Variant, PromoCode, Order, OrderItem


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'abbreviation']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'url_key', 'description', 'image']


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'sku', 'qty_in_stock', 'color', 'size', 'image']


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'description', 'category', 'url_key', 'variants', 'season', 'year']

    def create(self, validated_data):
        variants = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)

        short_brand = product.brand.abbreviation
        short_year = str(product.year)
        print(short_year)
        short_product_name = product.name[0:3]
        for variant in variants:
            sku = f'{short_brand}{product.season}{short_year[2:]}-{short_product_name}-{variant["size"]}{variant["color"]}'
            Variant.objects.create(product=product, sku=sku.upper(), **variant)
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



