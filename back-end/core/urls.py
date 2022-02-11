from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet, ProfileViewSet, AddressViewSet
from store.views.products import ProductEditDeleteView, ProductCreateView, ProductListView
from store.views.brands import BrandCreateView, BrandEditDeleteView, BrandListView
from store.views.categories import CategoryListView, CategoryCreateView, CategoryEditDeleteView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Public
    path('api/brands/', BrandListView.as_view()),
    path('api/categories', CategoryListView.as_view()),
    path('api/products', ProductListView.as_view()),
    # Brands
    path('api/admin/brands', BrandCreateView.as_view()),
    path('api/admin/brands/<pk>', BrandEditDeleteView.as_view()),
    # Categories
    path('api/admin/categories', CategoryCreateView.as_view()),
    path('api/admin/categories/<pk>', CategoryEditDeleteView.as_view()),
    # Products
    path('api/admin/products', ProductCreateView.as_view()),
    path('api/admin/products/<pk>', ProductEditDeleteView.as_view()),
    # Other
    path('api-auth/', include('rest_framework.urls')),
]
