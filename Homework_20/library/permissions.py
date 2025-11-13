from rest_framework import permissions


class IsAdminOrReadCreateUpdate(permissions.BasePermission):
    """
    allows:
        GET, HEAD, OPTIONS, POST PUT, PATCH for authenticated user;
        DELETE for staff user;
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False  # block everything for anonymous users
        if request.method == 'DELETE':
            return request.user.is_staff # admin can do DELETE
        return True  # authenticated users can do GET, HEAD, OPTIONS, POST PUT, PATCH

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
