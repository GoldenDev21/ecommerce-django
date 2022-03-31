from rest_framework import serializers
from django.db import transaction
from .models import Brand, Category, Product, Variant, PromoCode, Order, OrderItem
from .utils import create_sku, update_instance


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'abbreviation']

    def create(self, validated_data):
        abbreviation = validated_data.pop("abbreviation")
        brand = Brand.objects.create(abbreviation=abbreviation.upper(), **validated_data)
        return brand

    def update(self, instance, validated_data):
        brand = update_instance(instance, ['name'], validated_data)
        if "abbreviation" in validated_data:
            brand.abbreviation = validated_data['abbreviation'].upper()
        brand.save()
        return brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class VariantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Variant
        fields = ['id', 'sku', 'qty_in_stock', 'color', 'size', 'image']


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ProductSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'description', 'category', 'url_key', 'variants', 'season', 'year']

    def create(self, validated_data):
        variants = validated_data.pop('variants', [])
        with transaction.atomic():
            product = Product.objects.create(**validated_data)
            for variant in variants:
                sku = create_sku(product, variant)
                if Variant.objects.filter(sku=sku).exists():
                    raise serializers.ValidationError("SKU must be unique")
                Variant.objects.create(product=product, sku=sku, **variant)
        return product

    def update(self, instance, validated_data):
        variants = validated_data.pop('variants', [])
        new_variants = [variant for variant in variants if variant['id'] is None]
        updated_variants = [variant for variant in variants if variant['id'] is not None]

        with transaction.atomic():
            product = update_instance(
                instance,
                ['name', 'brand', 'price', 'description', 'category', 'season', 'year'],
                validated_data)
            product.save()

            for variant in new_variants:
                sku = create_sku(product, variant)
                Variant.objects.create(product=product, sku=sku, **variant)

            for variant in updated_variants:
                variant_instance = Variant.objects.filter(pk=variant['id']).first()
                if variant_instance:
                    new_variant = update_instance(variant_instance, ['image', 'qty_in_stock'], variant)
                    if variant.get('size') or variant.get('color'):
                        raise serializers.ValidationError('Cannot update size or color on an existing variant.')
                    new_variant.save()

        return product


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ['id', 'active', 'code', 'discount_percent', 'type', 'expiration_date']


class OrderItemSerializer(serializers.ModelSerializer):
    variant = VariantSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'variant', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'items', 'updated_at', "shipping_method"]

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order

    def update(self, instance, validated_data):
        if 'items' in validated_data:
            raise serializers.ValidationError('Order items can only be updated via the order-items endpoint.')
        else:
            order = update_instance(instance, ['status'], validated_data)
            order.save()
        return order



