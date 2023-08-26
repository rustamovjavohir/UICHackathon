from rest_framework import serializers

from api.files.serializers import ImageSerializer
from apps.file.models import Image
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

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')
        photoUrls_data = validated_data.pop('photoUrls')
        category = Category.objects.get_or_create(**category_data)[0]
        tags = [Tag.objects.get_or_create(**tag_data)[0] for tag_data in tags_data]
        photoUrls = [Image.objects.get_or_create(**photoUrl_data)[0] for photoUrl_data in photoUrls_data]

        pet = Pet.objects.create(category=category, **validated_data)
        pet.tags.set(tags)
        pet.photoUrls.set(photoUrls)
        return pet
