from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active','is_superuser')
    list_filter = ('email', 'is_staff', 'is_active','is_superuser')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )

admin.site.register(User , CustomUserAdmin)
admin.site.register(Profile)