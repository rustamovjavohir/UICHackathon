from django.contrib import admin

from apps.auth_user.models import User, UserStatus, Customer
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin


@admin.register(User)
class UserAdmin(AbstractUserAdmin):
    list_display = ('id', 'username', 'musk_phone_number', 'email', 'fullName', 'is_active', 'is_staff', 'is_superuser',
                    'is_client')
    list_display_links = ('id', 'username')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('phone', 'email')
    ordering = ('-id', 'is_staff')
    fieldsets = (
        ('Персональная информация', {'fields': ('fullName', 'profilePhoto')}),
        (None, {'fields': ('email', 'phone', 'password')}),
        ('Разрешения', {'fields': ('groups', 'user_permissions')}),
        ('Роль пользователя', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_client')}),
        ('Информация о дате', {'fields': ('last_login', 'date_joined', 'created_at')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Groups', {'fields': ('groups',)}),

    )
    readonly_fields = ('musk_phone_number', 'date_joined', 'last_login', 'created_at')

    def musk_phone_number(self, obj):
        return obj.musk_phone_number

    musk_phone_number.short_description = 'Номер телефона'


@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at')
    list_display_links = ('id', 'status')
    readonly_fields = ('created_at',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_display_links = ('id', 'user')
    readonly_fields = ('created_at',)
