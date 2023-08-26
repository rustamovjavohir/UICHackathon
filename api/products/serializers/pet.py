from rest_framework import serializers

from api.files.serializers import ImageSerializer
from apps.product.models import (Pet, Tag, Category)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'parent',
            'updated_at',
            'created_at',
        )
        read_only_fields = (
            'id',
            'slug',
            'updated_at',
            'created_at',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug',
            'updated_at',
            'created_at',
        )
        read_only_fields = (
            'id',
            'slug',
            'updated_at',
            'created_at',
        )


class PetSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    photoUrls = ImageSerializer(many=True)

    class Meta:
        model = Pet
        fields = (
            'id',
            'name',
            'category',
            'photoUrls',
            'tags',
            'status',
            'updated_at',
            'created_at',
        )
        read_only_fields = (
            'id',
            'updated_at',
            'created_at',
        )
