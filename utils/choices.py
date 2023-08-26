from django.db.models import TextChoices


class UserRoleChoices(TextChoices):
    ADMIN = "admin", "Администратор"
    SUPER_ADMIN = "super_admin", "Супер администратор"
    DIRECTOR = "director", "Директор"
    MANAGER = "manager", "Менеджер"
    SUPER_MANAGER = "super_manager", "Супер менеджер"
    OPERATOR = "operator", "Оператор"
    SUPER_OPERATOR = "super_operator", "Супер оператор"
    ACCOUNTING = "accounting", "Бухгалтерия"

    DRIVER = "driver", "Водитель"

    CLIENT = "client", "Клиент"


class AuthStatusChoices(TextChoices):
    NEW = "new", "Новый"
    VERIFY = "verify", "На проверке"
    HALF_DONE = "half_done", "Частично заполнен"
    DONE = "done", "Заполнен"


class ClientStatusChoices(TextChoices):
    NEW = "new", "Новый"
    PENDING = "pending", "Ожидает"
    VERIFY = "verify", "На проверке"
    HALF_DONE = "half_done", "Частично заполнен"
    DONE = "done", "Заполнен"
    BLOCKED = "blocked", "Заблокирован"
    DELETED = "deleted", "Удален"
    ARCHIVED = "archived", "Архивирован"


class LangChoices(TextChoices):
    UZ = "uz", "O'zbekcha"
    RU = "ru", "Русский"
    EN = "en", "English"


class RegionChoices(TextChoices):
    TASHKENT = "tashkent", "Ташкент"
    ANDIJAN = "andijan", "Андижан"
    BUKHARA = "bukhara", "Бухара"
    DJIZAK = "djizak", "Джизак"
    KASHKADARYA = "kashkadarya", "Кашкадарья"
    NAMANGAN = "namangan", "Наманган"
    NAVOI = "navoi", "Навои"
    SAMARKAND = "samarkand", "Самарканд"
    SURKHANDARYA = "surkhandarya", "Сурхандарья"
    SYRDARYA = "syrdarya", "Сырдарья"
    FERGANA = "fergana", "Фергана"
    KHOREZM = "khorezm", "Хорезм"
    KARAKALPAKSTAN = "karakalpakstan", "Каракалпакстан"
    TASHKENT_REGION = "tashkent_region", "Ташкентская область"


class PetStatusChoices(TextChoices):
    AVAILABLE = "available", "Доступен"
    PENDING = "pending", "Ожидает"
    SOLD = "sold", "Продан"
