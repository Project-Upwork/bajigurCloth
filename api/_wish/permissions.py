from rest_framework import permissions

class MemberAccessPermission(permissions.BasePermission):
    def has_permission(self,request, view):
        return True

        
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Hanya admin yang bisa write data
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False