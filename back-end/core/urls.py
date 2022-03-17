from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserListCreateView, UserRetrieveEditDestroyView, UserRetrieveEditView, UserCreateView
from store.views.products import ProductEditDeleteView, ProductCreateView, ProductListView, ProductDetailView
from store.views.variants import VariantEditDeleteView
from store.views.brands import BrandCreateView, BrandEditDeleteView, BrandListView, BrandDetailView
from store.views.categories import CategoryListView, CategoryCreateView, CategoryEditDeleteView, CategoryDetailView
from store.views.promo_codes import PromoCodeListCreateView, PromoCodeEditDeleteView
from store.views.orders import OrderEditView, OrderListCreateView, OrderRetrieveEditDeleteView

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Public
    path('api/brands/<pk>/', BrandDetailView.as_view()),
    path('api/brands/', BrandListView.as_view()),
    path('api/categories/<pk>/', CategoryDetailView.as_view()),
    path('api/categories/', CategoryListView.as_view()),
    path('api/products/<pk>/', ProductDetailView.as_view()),
    path('api/products/', ProductListView.as_view()),
    path('api/orders/<pk>/', OrderEditView.as_view()),
    path('api/orders/', OrderListCreateView.as_view()),
    path('api/users/<pk>/', UserRetrieveEditView.as_view()),
    path('api/users/', UserCreateView.as_view()),
    # Admin
    # Brands
    path('api/admin/brands/', BrandCreateView.as_view()),
    path('api/admin/brands/<pk>/', BrandEditDeleteView.as_view()),
    # Categories
    path('api/admin/categories/', CategoryCreateView.as_view()),
    path('api/admin/categories/<pk>/', CategoryEditDeleteView.as_view()),
    # Orders
    path('api/admin/orders/<pk>/', OrderRetrieveEditDeleteView.as_view()),
    path('api/admin/orders/', OrderListCreateView.as_view()),
    # Products
    path('api/admin/products/', ProductCreateView.as_view()),
    path('api/admin/products/<pk>/', ProductEditDeleteView.as_view()),
    path('api/admin/products/variants/<pk>', VariantEditDeleteView.as_view()),
    # Promo Codes
    path('api/admin/promo_codes/', PromoCodeListCreateView.as_view()),
    path('api/admin/promo_codes/<pk>/', PromoCodeEditDeleteView.as_view()),
    # Users
    path('api/admin/users/', UserListCreateView.as_view()),
    path('api/admin/users/<pk>/', UserRetrieveEditDestroyView.as_view()),
    # Other
    path('api-auth/', include('rest_framework.urls')),
]
