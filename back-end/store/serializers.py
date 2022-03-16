from rest_framework import serializers

from .models import Brand, Category, Product, Variant, PromoCode, Order, OrderItem
from .utils import create_sku, update_instance


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'abbreviation']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'url_key', 'description', 'image']


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
        variants = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)

        for variant in variants:
            sku = create_sku(product, variant)
            if Variant.objects.filter(sku=sku).exists():
                raise serializers.ValidationError("SKU must be unique")
            Variant.objects.create(product=product, sku=sku, **variant)
        return product

    def update(self, instance, validated_data):
        new_instance = update_instance(
            instance,
            ['name', 'brand', 'price', 'description', 'category', 'season', 'year'],
            validated_data)
        new_instance.save()

        if 'variants' in validated_data:
            variant_data = validated_data.pop('variants')
            for variant_obj in variant_data:
                if 'id' not in variant_obj:
                    sku = create_sku(new_instance, variant_obj)
                    Variant.objects.create(product=new_instance, sku=sku, **variant_obj)
                else:
                    existing_variant = Variant.objects.filter(pk=variant_obj['id']).first()
                    if existing_variant:
                        new_variant = update_instance(existing_variant, ['image', 'qty_in_stock'], variant_obj)
                        if variant_obj.get('size') or variant_obj.get('color'):
                            raise serializers.ValidationError('Cannot update size or color on an existing variant.')
                        new_variant.save()

        return new_instance


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
    user = serializers.ReadOnlyField(source='user.id')
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'items', 'updated_at']

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order



