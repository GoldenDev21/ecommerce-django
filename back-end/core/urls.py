from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet, ProfileViewSet, AddressViewSet
from store.views.products import product_edit_delete_view, product_create_view, products_list_view
from store.views.brands import brand_create_view, brand_edit_delete_view, brands_list_view
from store.views.categories import CategoryListView, CategoryEditView, CategoryCreateView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Public
    path('api/brands/', brands_list_view),
    path('api/categories', CategoryListView.as_view()),
    path('api/products', products_list_view),
    # Brands
    path('api/admin/brands', brand_create_view),
    path('api/admin/brands/<pk>', brand_edit_delete_view),
    # Categories
    path('api/admin/categories', CategoryCreateView.as_view()),
    path('api/admin/categories/<pk>', CategoryEditView.as_view()),
    # Products
    path('api/admin/products', product_create_view),
    path('api/admin/products/<pk>', product_edit_delete_view),
    # Other
    path('api-auth/', include('rest_framework.urls')),
]
