from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import User
from .serializers import UserSerializer


@extend_schema_view(
    list=extend_schema(summary='List all users', tags=['Users']),
    retrieve=extend_schema(summary='Get user details', tags=['Users']),
    create=extend_schema(summary='Create new user', tags=['Users']),
    update=extend_schema(summary='Update user', tags=['Users']),
    partial_update=extend_schema(summary='Partially update user', tags=['Users']),
    destroy=extend_schema(summary='Delete user', tags=['Users']),
)
class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.
    Provides CRUD operations for user management.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter queryset to only return current user.
        """
        return User.objects.filter(id=self.request.user.id)


class UserProfileView(APIView):
    """
    API view to get current user's profile.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary='Get current user profile',
        tags=['Users'],
        responses={200: UserSerializer}
    )
    def get(self, request):
        """
        Return current user's profile.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
