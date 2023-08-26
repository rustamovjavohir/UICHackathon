from rest_framework import serializers
from apps.auth_user.models import (User, UserStatus)


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = (
            'id',
            'status'
        )
        read_only_fields = (
            'id',
        )


class UserSerializer(serializers.ModelSerializer):
    # userStatus = UserStatusSerializer()  # TODO maybe changes

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'firstName',
            'lastName',
            'email',
            'password',
            'phone',
            'userStatus'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = (
            'id',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'firstName',
            'lastName',
            'email',
            'phone',
            'password',
            'userStatus'
        )
        read_only_fields = (
            'id',
            'password',
        )


class BulkCreateUserSerializers(serializers.Serializer):
    users = UserSerializer(many=True)

    def create(self, validated_data):
        users = [User(**item) for item in validated_data['users']]
        return User.objects.bulk_create(users)
