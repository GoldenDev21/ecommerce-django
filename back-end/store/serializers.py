import decimal

from rest_framework import serializers
from django.db import transaction
from .models import Brand, Product, Variant, PromoCode, Order, OrderItem
from .utils import create_sku, update_instance, get_shipping_price


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "abbreviation"]

    def create(self, validated_data):
        abbreviation = validated_data.pop("abbreviation")
        brand = Brand.objects.create(
            abbreviation=abbreviation.upper(), **validated_data
        )
        return brand

    def update(self, instance, validated_data):
        brand = update_instance(instance, ["name"], validated_data)
        if "abbreviation" in validated_data:
            brand.abbreviation = validated_data["abbreviation"].upper()
        brand.save()
        return brand


class VariantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Variant
        fields = ["id", "sku", "qty_in_stock", "color", "size", "image"]
        read_only_fields = ["sku"]  # TODO: Do not allow color & size updates


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    def __init__(self, *args, **kwargs):
        kwargs["partial"] = True
        super(ProductSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "brand",
            "price",
            "description",
            "category",
            "url_key",
            "variants",
            "season",
            "year",
            "department",
            "active",
            "in_stock"
        ]

    def create(self, validated_data):
        variants = validated_data.pop("variants", [])
        with transaction.atomic():
            product = Product.objects.create(**validated_data)
            for variant in variants:
                sku = create_sku(product, variant)
                if Variant.objects.filter(sku=sku).exists():
                    raise serializers.ValidationError("SKU must be unique")
                Variant.objects.create(product=product, sku=sku, **variant)
        return product

    def update(self, instance, validated_data):
        if "variants" in validated_data:
            raise serializers.ValidationError(
                "Variants can only be updated via the variants endpoint."
            )
        else:
            product = update_instance(
                instance,
                ["name", "brand", "price", "description", "category", "season", "year", "department", "active"],
                validated_data,
            )
            product.save()
        return product


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ["id", "active", "code", "discount_percent", "type", "expiration_date"]


class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(required=False, max_digits=7, decimal_places=2)
    name = serializers.CharField(required=False)
    brand = serializers.CharField(required=False)
    sku = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = OrderItem
        fields = ["id", "quantity", "price", "name", "brand", "sku", "variant", "image"]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "status",
            "created_at",
            "items",
            "updated_at",
            "shipping_method",
            "subtotal",
            "total",
            "shipping_total",
            "billing_address",
            "shipping_address",
        ]
        read_only_fields = ["shipping_total", "total", "subtotal"]

    def create(self, validated_data):
        with transaction.atomic():
            items = validated_data.pop("items")
            order = Order.objects.create(**validated_data)

            prices = []
            for item in items:
                variant_pk = item.get("variant").pk
                variant = Variant.objects.filter(pk=variant_pk)[0]
                product = Product.objects.filter(pk=variant.product_id)[0]
                selected_qty = item.get("quantity", 0)

                OrderItem.objects.create(
                    order=order,
                    price=product.price,
                    name=product.name,
                    image=variant.image,
                    brand=product.brand.name,
                    sku=variant.sku,
                    **item
                )
                prices.append(product.price * selected_qty)
                variant.qty_in_stock -= selected_qty
                variant.save()
            subtotal = sum(prices)
            shipping_total = get_shipping_price(order.shipping_method)

            order.subtotal = subtotal
            order.shipping_total = shipping_total
            order.total = subtotal + decimal.Decimal(shipping_total)
            order.save()
        return order

    def update(self, instance, validated_data):
        if "items" in validated_data:
            raise serializers.ValidationError(
                "Order items can only be updated via the order-items endpoint."
            )
        else:
            order = update_instance(instance, ["status"], validated_data)
            order.save()
        return order
