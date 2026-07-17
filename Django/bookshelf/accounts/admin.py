from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('bio', 'profile_pic')})
    )

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
