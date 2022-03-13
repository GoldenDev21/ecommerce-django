from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings


class Brand(models.Model):
    name = models.CharField(max_length=40, unique=True)
    abbreviation = models.CharField(max_length=4, unique=True)
    url_key = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_key = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url_key = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_key = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    SEASON_CHOICES = [
        (1, 'Winter'),
        (2, 'Spring'),
        (3, 'Summer'),
        (4, 'Fall'),
    ]
    name = models.CharField(max_length=120, unique=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    season = models.PositiveSmallIntegerField(choices=SEASON_CHOICES)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=1500)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    url_key = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_key = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Variant(models.Model):

    COLOR_CHOICES = [
        ('BLK', 'Black'),
        ('CRM', 'Cream'),
        ('PNK', 'Pink'),
        ('BRN', 'Brown'),
        ('GRY', 'Grey'),
        ('BLU', 'Blue'),
        ('GRN', 'Green'),
        ('WHT', 'White'),
        ('SLV', 'Silver'),
        ('GLD', 'Gold'),
        ('ORN', 'Orange'),
        ('YLL', 'Yellow'),
        ('RED', 'Red'),
        ('PRP', 'Purple'),
        ('MLT', 'Multi')
    ]

    SIZE_CHOICES = [
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('ONE', 'One Size'),
        ('32', '32'),
        ('34', '34'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
    ]

    sku = models.CharField(max_length=24, unique=True, blank=True)
    qty_in_stock = models.IntegerField()
    color = models.CharField(max_length=4, choices=COLOR_CHOICES)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES)
    image = models.ImageField(blank=True)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)


class CustomDateTimeField(models.DateTimeField):

    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ""


class PromoCode(models.Model):
    PROMO_CODE_TYPES = [
        (1, 'Employee'),
        (2, 'Referral'),
        (3, 'Offer'),
        (4, 'New Customer')
    ]

    active = models.BooleanField(default=True)
    code = models.CharField(max_length=10, unique=True)
    discount_percent = models.IntegerField()
    type = models.IntegerField(choices=PROMO_CODE_TYPES)
    expiration_date = CustomDateTimeField(blank=True, null=True)


class Order(models.Model):
    STATUS_CHOICES = [
        (1, 'Waiting for payment'),
        (2, 'Paid'),
        (3, 'Shipped'),
        (4, 'Delivered'),
        (5, 'Cancelled')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
