from rest_framework import permissions

from .models import UserRoles


class IsStudent(permissions.BasePermission):
    """
    Permission check for student role.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == UserRoles.STUDENT
        )

class IsCompany(permissions.BasePermission):
    """
    Permission check for organization role.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == UserRoles.COMPANY
        )

class RoleBasedPermission(permissions.BasePermission):
    """
    Generic role-based permission class that can be configured with allowed roles.
    """
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role in self.allowed_roles
        ) 

class RoleBasedObjectPermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role in self.allowed_roles
        )

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user and request.user.role in self.allowed_roles 