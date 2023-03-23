from rest_framework.permissions import BasePermissionMetaclass
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class BasePermission(metaclass=BasePermissionMetaclass):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True


class IsCook(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_active and IsAuthenticated:
            return True


class IsWaiter(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and IsAuthenticated:
            return True
        return bool(request.user and request.user.is_staff)


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser and IsAuthenticated:
            return True
