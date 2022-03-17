from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserListCreateView, UserRetrieveEditDestroyView, UserRetrieveEditView, UserCreateView
from store.views.products import ProductListCreateView, ProductRetrieveUpdateDestroyView
from store.views.variants import VariantRetrieveUpdateDestroyView
from store.views.brands import BrandListCreateView, BrandRetrieveUpdateDestroyView
from store.views.categories import CategoryListCreateView, CategoryRetrieveUpdateDestroyView
from store.views.promo_codes import PromoCodeListCreateView, PromoCodeRetrieveUpdateDestroyView
from store.views.orders import OrderEditView, OrderListCreateView, OrderRetrieveEditDeleteView

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/brands/<pk>/', BrandRetrieveUpdateDestroyView.as_view()),
    path('api/brands/', BrandListCreateView.as_view()),
    path('api/categories/<pk>/', CategoryRetrieveUpdateDestroyView.as_view()),
    path('api/categories/', CategoryListCreateView.as_view()),
    path('api/products/variants/<pk>', VariantRetrieveUpdateDestroyView.as_view()),
    path('api/products/<pk>/', ProductRetrieveUpdateDestroyView.as_view()),
    path('api/products/', ProductListCreateView.as_view()),
    path('api/promo_codes/<pk>/', PromoCodeRetrieveUpdateDestroyView.as_view()),
    path('api/promo_codes/', PromoCodeListCreateView.as_view()),
    path('api/orders/<pk>/', OrderEditView.as_view()),
    path('api/orders/', OrderListCreateView.as_view()),
    path('api/users/<pk>/', UserRetrieveEditView.as_view()),
    path('api/users/', UserCreateView.as_view()),
    # Admin
    # Orders
    path('api/admin/orders/<pk>/', OrderRetrieveEditDeleteView.as_view()),
    path('api/admin/orders/', OrderListCreateView.as_view()),
    # Users
    path('api/admin/users/', UserListCreateView.as_view()),
    path('api/admin/users/<pk>/', UserRetrieveEditDestroyView.as_view()),
    # Other
    path('api-auth/', include('rest_framework.urls')),
]
