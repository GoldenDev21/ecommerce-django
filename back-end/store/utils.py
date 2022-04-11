import re
import copy
from .models import ShippingMethodEnum


def create_sku(product, variant):
    short_product_name = re.sub(r"[aeiou\s]", "", product.name)[0:3]
    short_brand = product.brand.abbreviation
    short_year = str(product.year)[2:]
    sku = f'{short_brand}{product.season}{short_year}-{short_product_name}-{variant["size"]}{variant["color"]}'
    return sku.upper()


def get_shipping_price(shipping_type):
    """
    Temporary function to get shipping price before API is in place
    """
    if shipping_type == ShippingMethodEnum.POST:
        return 2.99
    elif shipping_type == ShippingMethodEnum.COURIER:
        return 5.99
    elif shipping_type == ShippingMethodEnum.EXPRESS:
        return 10.99
    else:
        return 0.00


def update_instance(instance, fields, validated_data):
    instance_copy = copy.deepcopy(instance)

    for field in fields:
        if field in validated_data:
            value = validated_data[field]
            setattr(instance_copy, field, value)
    return instance_copy
