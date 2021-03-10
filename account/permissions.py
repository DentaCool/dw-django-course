from rest_framework.permissions import BasePermission, IsAuthenticated


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return True

        
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in ("GET", ):
            return True
        if request.method in ("PUT", "UPDATE", "DELETE"):
            return IsAuthenticated().has_permission(request, view) and (obj is request.user)
        return True
