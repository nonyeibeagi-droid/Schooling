from rest_framework.permissions import BasePermission 
from accounts.models import User

class IsAdminUserRole(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == User.Role.ADMIN or request.user.is_superuser)

class IsTeacherUserRole(BasePermission):
    """
    Allows access only to teacher users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == User.Role.TEACHER)

class IsStudentUserRole(BasePermission):
    """
    Allows access only to student users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == User.Role.STUDENT)