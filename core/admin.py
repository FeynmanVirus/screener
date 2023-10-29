from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Screener

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = [
        (
            None,
            {
                "fields": ["email", "subscription_valid", "password"],
            },        ),
    ]
    list_display = ['email', 'username', 'subscription_valid', 'first_name', 'last_name', 'is_staff']

class ScreenerAdmin(admin.ModelAdmin):
    model = Screener
    fieldsets = [
        (
            None,
            {
                "fields": ["title", "clause"]
            }
        )
    ]
    list_display = ['title', 'clause']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Screener, ScreenerAdmin)    