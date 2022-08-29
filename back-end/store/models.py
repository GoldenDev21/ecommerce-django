from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings


class Category(models.IntegerChoices):
    # Clothing
    BLOUSES = 1,
    DRESSES = 2,
    JACKETS = 3,
    JEANS = 4,
    OUTERWEAR = 5,
    PANTS = 6,
    SETS = 7,
    SKIRTS = 8,
    SLEEPWEAR = 9,
    SPORTSWEAR = 10,
    SWEATERS = 11,
    T_SHIRTS = 12,
    # Footwear
    SANDALS = 13,
    HEELS = 14,
    SNEAKERS = 15,
    BOOTS = 16,
    BALLET_FLATS = 17,
    LOAFERS = 18,
    # Accessories
    BAGS = 19,
    SUNGLASSES = 20,
    JEWELRY = 21,
    WALLETS = 22,
    BELTS = 23,
    HATS = 24,
    SCARVES = 25


class Brand(models.Model):
    name = models.CharField(max_length=40, unique=True)
    abbreviation = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Season(models.IntegerChoices):
        WINTER = 1,
        SPRING = 2,
        SUMMER = 3,
        FALL = 4

    class Department(models.IntegerChoices):
        CLOTHING = 1,
        SHOES = 2,
        ACCESSORIES = 3

    name = models.CharField(max_length=120, unique=True)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    season = models.PositiveSmallIntegerField(choices=Season.choices)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=1500)
    department = models.PositiveSmallIntegerField(choices=Department.choices)
    category = models.PositiveSmallIntegerField(choices=Category.choices)
    url_key = models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slugified_name = slugify(self.name)
        if self.url_key != slugified_name:
            self.url_key = slugified_name
        super(Product, self).save(*args, **kwargs)


class Variant(models.Model):
    class Color(models.TextChoices):
        BLACK = 'BLK',
        BLUE = 'BLU',
        BEIGE = 'BEI',
        BROWN = 'BRN',
        GOLD = 'GLD',
        GREEN = 'GRN',
        GREY = 'GRY',
        IVORY = 'IVR',
        MULTI_COLORED = 'MLT',
        ORANGE = 'ORN',
        PINK = 'PNK',
        PURPLE = 'PRP',
        RED = 'RED',
        SILVER = 'SLV',
        TURQUOISE = 'TRQ',
        WHITE = 'WHT'
        YELLOW = 'YLL'

    SIZE_CHOICES = [
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("1", "One Size"),
        ("32", "32"),
        ("34", "34"),
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
    ]

    sku = models.CharField(max_length=24, unique=True, blank=True)
    qty_in_stock = models.IntegerField()
    color = models.CharField(max_length=4, choices=Color.choices)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES)
    image = models.ImageField(blank=True, null=True)
    product = models.ForeignKey(
        Product, related_name="variants", on_delete=models.CASCADE
    )


class CustomDateTimeField(models.DateTimeField):

    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ""


class PromoCode(models.Model):
    class PromoCodeType(models.IntegerChoices):
        EMPLOYEE = 1,
        REFERRAL = 2,
        OFFER = 3,
        NEW_CUSTOMER = 4

    active = models.BooleanField(default=True)
    code = models.CharField(max_length=10, unique=True)
    discount_percent = models.IntegerField()
    type = models.IntegerField(choices=PromoCodeType.choices)
    expiration_date = CustomDateTimeField(blank=True, null=True)

    def __str__(self):
        return self.code


class ShippingMethodEnum(models.IntegerChoices):
    POST = 1,
    COURIER = 2,
    EXPRESS = 3


class Order(models.Model):
    class Status(models.IntegerChoices):
        AWAITING_PAYMENT = 1,
        PAYMENT_RECEIVED = 2,
        SHIPPED = 3,
        DELIVERED = 4,
        CANCELLED = 5

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=Status.choices, default=Status.AWAITING_PAYMENT
    )
    promo_code = models.ForeignKey(
        PromoCode, on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_method = models.IntegerField(choices=ShippingMethodEnum.choices)
    subtotal = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    shipping_total = models.DecimalField(decimal_places=2, max_digits=7, null=True)

    def __str__(self):
        return self.id


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    name = models.CharField(max_length=255, default="")
    brand = models.CharField(max_length=255, default="")
    sku = models.CharField(max_length=255, default="")
    image = models.ImageField(blank=True, null=True)
