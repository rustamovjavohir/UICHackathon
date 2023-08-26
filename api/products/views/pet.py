from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from apps.product.models import Pet
from apps.auth_user.permissions import IsSuperUser
from api.products.serializers.pet import PetSerializer
from utils.choices import PetStatusChoices
from utils.exceptions import NotFoundException
from utils.paginations import BasePagination
from utils.responses import Response
from utils.swagger_tags import Web
from api.mixins import (ReturnResponseMixin, ActionPermissionMixin, ActionSerializerMixin, HandleExceptionMixin)


class PetViewSet(ActionSerializerMixin, ActionPermissionMixin, ReturnResponseMixin, ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    pagination_class = BasePagination
    filer_fields = ['status']

    ACTION_SERIALIZERS = {
        'list': PetSerializer,
        'retrieve': PetSerializer,
        'update': PetSerializer,
        'partial_update': PetSerializer,
        'create': PetSerializer,
    }
    ACTION_PERMISSIONS = {
        'list': [AllowAny],
        'create': [AllowAny],
        'retrieve': [IsAuthenticated],
        'destroy': [IsSuperUser],
        'update': [IsAuthenticated],
        'partial_update': [IsAuthenticated],
        'find_by_status': [AllowAny],
        'find_by_tags': [AllowAny],
    }

    @extend_schema(tags=[Web.Pet.PREFIX], summary='Add a new pet to the store')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=[Web.Pet.PREFIX], summary='Get list of pets')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=[Web.Pet.PREFIX], summary='Find pet by ID')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=[Web.Pet.PREFIX], summary='Deletes a pet')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(tags=[Web.Pet.PREFIX], summary='Update an existing pet')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=[Web.Pet.PREFIX], summary='Update an existing pet (particular fields)')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=False, url_path='findByStatus', url_name='findByStatus')
    @extend_schema(tags=[Web.Pet.PREFIX], summary='Finds Pets by tags',
                   parameters=PetStatusChoices.get_values())
    def find_by_status(self, request, *args, **kwargs):
        """
        Headers:
            - status: available, pending, sold
        """
        status = request.query_params.get('status')
        if status not in PetStatusChoices.get_values():
            raise Exception('Invalid status')
        queryset = self.get_queryset().filter(status=status)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)

    @action(methods=['get'], detail=False, url_path='findByTags', url_name='findByTags')
    @extend_schema(tags=[Web.Pet.PREFIX], summary='Finds Pets by tags')
    def find_by_tags(self, request, *args, **kwargs):
        """
        Headers:
            - tags: tag1, tag2, tag3
        """
        tags = request.query_params.get('tags')
        if not tags:
            raise NotFoundException('Invalid tags')
        if self.queryset.filter(tags__name__in=tags.split(',')).count() == 0:
            raise NotFoundException('Not found')
        queryset = self.get_queryset().filter(tags__name__in=tags.split(','))
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)
