from django.contrib import admin

from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_active",
    )


admin.site.register(User, CustomUserAdmin)
