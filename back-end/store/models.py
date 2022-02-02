from django.db import models
from django.template.defaultfilters import slugify


class Brand(models.Model):
    name = models.CharField(max_length=40, unique=True)
    abbreviation = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=3, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url_key = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_key = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    url_key = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_key = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(max_length=1500)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    url_key = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_key = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Variant(models.Model):
    SIZE_CHOICES = [
        (1, 'One Size'),
        (2, 'XS'),
        (3, 'S'),
        (4, 'M'),
        (5, 'L'),
        (6, 'XL'),
        (65, '6.5'),
        (70, '7'),
        (75, '7.5'),
        (80, '8'),
        (85, '8.5'),
        (90, '9'),
        (95, '9.5'),
        (100, '10'),
        (105, '10.5'),
        (110, '11'),
        (115, '11.5'),
    ]

    sku = models.CharField(max_length=24, unique=True)
    qty_in_stock = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.IntegerField(choices=SIZE_CHOICES)
    image = models.ImageField()
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        sku = f'{self.product.id}{self.product.brand.abbreviation}{self.size}{self.color.abbreviation}'
        self.sku = sku.upper()
        super(Product, self).save(*args, **kwargs)


class PromoCode(models.Model):
    PROMO_CODE_TYPES = [
        (1, 'Employee'),
        (2, 'Referral'),
        (3, 'Offer'),
        (4, 'New Customer')
    ]

    active = models.BooleanField()
    code = models.CharField(max_length=10, unique=True)
    discount_percent = models.IntegerField()
    type = models.IntegerField(choices=PROMO_CODE_TYPES)


class Order(models.Model):
    STATUS_CHOICES = [
        (1, 'Waiting for payment'),
        (2, 'Paid'),
        (3, 'Shipped'),
        (4, 'Delivered'),
        (5, 'Cancelled')
    ]
    profile = models.ForeignKey('accounts.Profile', related_name='orders', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)
    discount_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
