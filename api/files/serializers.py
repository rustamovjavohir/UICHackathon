from rest_framework import serializers
from apps.file.models import (Image)


class ImageSerializer(serializers.ModelSerializer):
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
