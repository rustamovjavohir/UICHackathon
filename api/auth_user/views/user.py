from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from api.auth_user.paginations import UserPagination
from apps.auth_user.models import User
from apps.auth_user.permissions import IsSuperUser
from api.auth_user.serializers.user import UserSerializer, BulkCreateUserSerializers, UserUpdateSerializer
from utils.responses import Response
from utils.swagger_tags import Web

from api.mixins import (ReturnResponseMixin, ActionPermissionMixin, ActionSerializerMixin, HandleExceptionMixin)


class UserViewSet(ActionSerializerMixin, ActionPermissionMixin, ReturnResponseMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    ACTION_SERIALIZERS = {
        'list': UserSerializer,
        'retrieve': UserSerializer,
        'update': UserUpdateSerializer,
        'partial_update': UserUpdateSerializer,
        'create': UserSerializer,
    }
    ACTION_PERMISSIONS = {
        'list': [AllowAny],
        'create': [AllowAny],
        'retrieve': [IsAuthenticated],
        'destroy': [IsSuperUser],
        'update': [IsAuthenticated],
        'partial_update': [IsAuthenticated],
    }

    @extend_schema(tags=[Web.User.PREFIX], summary='Create user')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=[Web.User.PREFIX], summary='Get list user')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=[Web.User.PREFIX], summary='Get user by user name')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=[Web.User.PREFIX], summary='Delete user')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(tags=[Web.User.PREFIX], summary='Update user')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=[Web.User.PREFIX], summary='Update user')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class UserCreateBulk(HandleExceptionMixin, GenericAPIView):
    """
    Create bulk user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=[Web.User.PREFIX], summary='Creates list of users with given input array')
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
