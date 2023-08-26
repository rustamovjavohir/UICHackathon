from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from apps.order.models import Address
from utils.choices import UserRoleChoices, ClientStatusChoices, LangChoices
from utils.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_client(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_client', True)
        extra_fields.setdefault('is_active', True)
        if email:
            email = email.lower()
        return self.create_user(username, email, password, **extra_fields)

    def create_staff(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        email = email.lower()
        return self.create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **extra_fields)


def phone_validator(value):
    format_text = 'Номер телефона должен быть в формате: 998 XX XXX XX XX'
    if not value.isdigit():
        raise ValidationError(f'Номер телефона должен состоять только из цифр.\n{format_text}')
    elif len(value) != 12:
        raise ValidationError(f'Номер телефона должен состоять из 12 цифр.\n{format_text}')
    elif not value.startswith('998'):
        raise ValidationError(f'Номер телефона должен начинаться с (998).\n{format_text}')


class UserStatus(BaseModel):
    status = models.CharField(max_length=26,
                              choices=ClientStatusChoices.choices,
                              default=ClientStatusChoices.NEW,
                              verbose_name='Auth Статус')

    class Meta:
        verbose_name = 'Пользователь Статус'
        verbose_name_plural = 'Пользователь Статусы'

    def __str__(self):
        return self.status


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    fullName = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО')
    firstName = models.CharField(max_length=255,
                                 blank=True, null=True,
                                 verbose_name='Имя')
    lastName = models.CharField(max_length=255,
                                blank=True, null=True,
                                verbose_name='Фамилия')
    phone = models.CharField(max_length=12, unique=True, validators=[phone_validator],
                             help_text='Номер телефона должен быть в формате: 998 XX XXX XX XX',
                             verbose_name='Номер телефона')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    profilePhoto = models.ImageField(upload_to='user/profile_photos', null=True, blank=True,
                                     verbose_name='Фото профиля',
                                     default='user/profile_photos/default.png')
    username = models.CharField(max_length=20,
                                verbose_name='Логин',
                                unique=True)
    userStatus = models.ForeignKey(UserStatus,
                                   related_name='userStatus',
                                   on_delete=models.SET_NULL,
                                   null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_client = models.BooleanField(default=False, verbose_name='Клиент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата изменения')

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.username} - {self.musk_phone_number}"

    @property
    def musk_phone_number(self):
        """Маскированный номер телефона as +998(93) 123-45-67"""
        return f"+{self.phone[:3]}({self.phone[3:5]}) " \
               f"{self.phone[5:8]}-{self.phone[8:10]}-{self.phone[10:]}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    objects = UserManager()


class UserRole(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='userRole',
                             verbose_name='Пользователь')
    role = models.CharField(max_length=26,
                            choices=UserRoleChoices.choices,
                            default=UserRoleChoices.CLIENT,
                            verbose_name='Роли пользователей')

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'

    def __str__(self):
        return f'{self.role} - {self.user}'


class Customer(BaseModel):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='user_client',
                                null=True, blank=True,
                                verbose_name='Пользователь')
    status = models.CharField(max_length=26,
                              choices=ClientStatusChoices.choices,
                              default=ClientStatusChoices.NEW,
                              verbose_name='Auth Статус')
    address = models.ForeignKey(Address,
                                on_delete=models.SET_NULL,
                                null=True, blank=True,
                                add_help_text='Адрес',
                                verbose_name='Адрес')
    lang = models.CharField(max_length=2,
                            choices=LangChoices.choices,
                            default=LangChoices.UZ,
                            verbose_name="Язык", )

    class Meta:
        verbose_name = 'Клиент пользователь'
        verbose_name_plural = 'Клиент пользователи'

    def __str__(self):
        return f'{self.user}'
