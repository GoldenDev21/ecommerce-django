import re


def create_sku(product, variant):
    short_product_name = re.sub(r'[aeiou\s]', "", product.name)[0:3]
    short_brand = product.brand.abbreviation
    short_year = str(product.year)[2:]
    sku = f'{short_brand}{product.season}{short_year}-{short_product_name}-{variant["size"]}{variant["color"]}'
    return sku.upper()
