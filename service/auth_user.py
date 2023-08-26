from apps.auth_user.models import Customer, User
from repository.auth_user import UserRepository


class UserServices:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_by_uniq_id(self, identity: int) -> User:
        return self.user_repository.get_user_by_uniq_id(identity)

    def get_user_by_phone_number(self, phone_number: str) -> User:
        return self.user_repository.get_user_by_phone_number(phone_number)

    def get_client_by_phone_number(self, phone_number: str) -> Customer:
        return self.user_repository.get_client_by_phone_number(phone_number)

    def get_jwt_tokens_for_user(self, user):
        return self.user_repository.get_jwt_tokens_for_user(user)

    def set_user_password(self, user, password):
        return self.user_repository.set_new_password(user, password)
