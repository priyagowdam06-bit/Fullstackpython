from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active'] # FIX 1: 'its_staff' -> 'is_staff'
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('bio', 'profile_pic')}), # FIX 2: syntax: fields: and proper braces
    )

admin.site.register(CustomUser, CustomUserAdmin)