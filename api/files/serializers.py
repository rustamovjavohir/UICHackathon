from rest_framework import serializers
from apps.file.models import (Image)
from PIL import Image as Img
from drf_extra_fields.fields import Base64ImageField


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Image
        fields = (
            'id',
            'name',
            'image',
            'is_main',
            'updated_at',
            'created_at',
        )
        read_only_fields = (
            'id',
            'updated_at',
            'created_at',
        )
