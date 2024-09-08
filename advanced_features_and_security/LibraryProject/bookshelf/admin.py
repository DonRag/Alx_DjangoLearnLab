from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'date_of_birth', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
