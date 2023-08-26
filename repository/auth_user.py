import random

from django.shortcuts import get_object_or_404

from apps.auth_user import constants
from apps.auth_user.models import User, UserRole, Customer
from utils.generates import generate_unique_code
from rest_framework_simplejwt import tokens


class UserRepository:
    def __init__(self):
        self.user = User
        self.user_role = UserRole
        self.user_client = Customer
        self.sms_repository = None

    def get_user_by_uniq_id(self, identity: int) -> User:
        if self.user_client.objects.filter(client_id=identity, is_active=True).exists():
            return self.user_client.objects.get(client_id=identity).user
        raise self.user.DoesNotExist(constants.USER_DOES_NOT_EXIST)

    def get_user_by_phone_number(self, phone: str) -> User:
        return get_object_or_404(self.user, phone=phone)

    def get_client_by_phone_number(self, phone: str) -> Customer:
        return self.get_user_by_phone_number(phone).user_client

    def get_user_by_email(self, email: str) -> User:
        return get_object_or_404(self.user, email=email)

    def get_user_by_username(self, username: str) -> User:
        return get_object_or_404(self.user, username=username)

    @staticmethod
    def set_new_password(user, password) -> User:
        user.set_password(password)
        user.save()
        return user

    def send_sms(self, phone_number, code):
        user = self.get_user_by_phone_number(phone_number)
        code = generate_unique_code(length=4) if code is None else code
        self.sms_repository.send_sms(user, code)
        pass  # TODO: send sms logic

    def verify_sms(self, phone_number, code) -> bool:
        user = self.get_user_by_phone_number(phone_number)
        return self.sms_repository.is_valid_sms(user, code)

    def get_jwt_tokens_for_user(self, user: User) -> dict:
        return {
            'access': str(tokens.AccessToken.for_user(user)),
            'refresh': str(tokens.RefreshToken.for_user(user)),
        }
