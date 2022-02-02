from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSet, ProfileViewSet, AddressViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
