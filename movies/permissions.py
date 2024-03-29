from rest_framework import permissions

class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False        