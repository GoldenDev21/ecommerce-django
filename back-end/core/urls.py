from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet, ProfileViewSet, AddressViewSet
from store.views import BrandListView, BrandCreateView, BrandEditView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/brands/', BrandListView.as_view()),
    path('api/admin/brands', BrandCreateView.as_view()),
    path('api/admin/brands/<pk>', BrandEditView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
