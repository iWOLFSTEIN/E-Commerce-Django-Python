from django.contrib import admin

from app_auth.models import Login, User, UserVerification
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    fieldsets = (
        (None, {"fields": ("id", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "is_verified",
                ),
            },
        ),
    )
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_verified",
        "is_staff",
    )
    list_filter = ("is_verified", "is_staff", "is_superuser", "groups")
    search_fields = ("id", "email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    def get_queryset(self, request):
        return super().get_queryset(request)

    def get_object(self, request, object_id, from_field=None):
        queryset = self.get_queryset(request)
        model = queryset.model
        # Replace 'id' with 'id' to fetch the correct object
        field = (
            model._meta.pk if from_field is None else model._meta.get_field(from_field)
        )
        try:
            return queryset.get(**{field.name: object_id})
        except model.DoesNotExist:
            return None


admin.site.register(User, UserAdmin)
admin.site.register(Login)
admin.site.register(UserVerification)
