from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'price': ['exact', 'gte', 'lte'],
            'name': ['exact', 'contains'],
            'variants__size': ['exact', 'in'],
            'brand': ['exact', 'in'],
            'variants__color': ['exact', 'in'],
            'active':  ['exact'],
            'in_stock': ['exact'],
            'variants__qty_in_stock': ['gte', 'lte']
        }
