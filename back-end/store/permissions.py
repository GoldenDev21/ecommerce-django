from rest_framework.permissions import BasePermission


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as an admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_staff:
            return True
        return False


class IsOwnerOrAdmin(BasePermission):
    """
    Object-level permission to only allow owners of an object or admins to read or edit the obj.
    Assumes the model instance has a `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
