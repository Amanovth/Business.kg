from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from django.contrib.auth.models import Group

from apps.accounts import models

admin.site.unregister(Group)

@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'get_avatar', 'name', 'email', 'phone', 'is_active', 'date_joined')
    ordering = ('-date_joined',)

    search_fields = ('username', 'name',)
    list_display_links = list_display

    readonly_fields = ('username', 'code',)

    fieldsets = (
        (_('Главная'), {'fields': ('mkg_id', 'username', 'name', 'email', 'phone', 'language', 'balance', 'password', '_avatar', 'description')}),
        (_('Права доступы'), {
            'fields': ('code', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Важные даты'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img style="border-radius: 50%;" src="{obj.avatar}" width="50" height="50" />')
        return "No Avatar"

    get_avatar.short_description = 'Avatar'


class DealerImagesInline(admin.StackedInline):
    model = models.DealerImages
    extra = 0

@admin.register(models.Dealer)
class DealerAdmin(admin.ModelAdmin):
  list_display = ("name", "type_dealer",)
  list_filter = ("type_dealer", "is_verified")
  inlines = (DealerImagesInline,)