from django.contrib import admin

from .models import Post


class CustomPostAdminMixin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "updated_at",
    ]


admin.site.register(Post, CustomPostAdminMixin)
