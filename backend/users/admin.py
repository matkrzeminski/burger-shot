from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, UserAddress


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "id",
        "uuid",
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "created",
        "is_staff",
        "is_active",
    )
    list_display_links = ("id", "uuid", "email")
    list_filter = (
        "first_name",
        "last_name",
        "created",
        "modified",
        "is_staff",
        "is_active",
    )
    search_fields = ("email", "phone_number", "first_name", "last_name")
    ordering = ("-modified",)
    fieldsets = (
        ("Credentials", {"fields": ("email", "password")}),
        ("Personal", {"fields": ("first_name", "last_name", "phone_number")}),
        (
            "Permissions and Groups",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created",
                    "last_login",
                )
            },
        ),
    )
    readonly_fields = ("created", "last_login")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    model = UserAddress
    list_display = (
        "id",
        "uuid",
        "street",
        "apartment",
        "postcode",
        "city",
        "country",
        "user",
        "created",
        "modified",
    )
    list_display_links = ("id", "uuid", "street")
    search_fields = ("street", "postcode")
    list_filter = ("city__name", "country__name", "postcode")
    ordering = ("modified",)
