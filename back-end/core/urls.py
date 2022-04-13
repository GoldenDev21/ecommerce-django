from django.urls import path, include
from rest_framework import routers
from accounts.views import (
    UserListCreateView,
    UserRetrieveEditDestroyView,
    UserCreateView,
    AddressRetrieveUpdateDestroyView,
    AddressListView,
)
from store.views.products import ProductListCreateView, ProductRetrieveUpdateDestroyView
from store.views.variants import VariantRetrieveUpdateDestroyView
from store.views.brands import BrandListCreateView, BrandRetrieveUpdateDestroyView
from store.views.categories import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
)
from store.views.promo_codes import (
    PromoCodeListCreateView,
    PromoCodeRetrieveUpdateDestroyView,
)
from store.views.orders import (
    OrderListCreateView,
    OrderRetrieveEditDeleteView,
    OrderItemRetrieveEditDestroyAPIView,
)

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("api/brands/<pk>/", BrandRetrieveUpdateDestroyView.as_view()),
    path("api/brands/", BrandListCreateView.as_view()),
    path("api/categories/<pk>/", CategoryRetrieveUpdateDestroyView.as_view()),
    path("api/categories/", CategoryListCreateView.as_view()),
    path("api/products/variants/<pk>", VariantRetrieveUpdateDestroyView.as_view()),
    path("api/products/<pk>/", ProductRetrieveUpdateDestroyView.as_view()),
    path("api/products/", ProductListCreateView.as_view()),
    path("api/promo-codes/<pk>/", PromoCodeRetrieveUpdateDestroyView.as_view()),
    path("api/promo-codes/", PromoCodeListCreateView.as_view()),
    path("api/orders/order-items/<pk>", OrderItemRetrieveEditDestroyAPIView.as_view()),
    path("api/orders/<pk>/", OrderRetrieveEditDeleteView.as_view()),
    path("api/orders/", OrderListCreateView.as_view()),
    path("api/users/addresses/<pk>", AddressRetrieveUpdateDestroyView.as_view()),
    path("api/users/addresses/", AddressListView.as_view()),
    path("api/users/new/", UserCreateView.as_view()),
    path("api/users/<pk>/", UserRetrieveEditDestroyView.as_view()),
    path("api/users/", UserListCreateView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]

# TODO JWT token
