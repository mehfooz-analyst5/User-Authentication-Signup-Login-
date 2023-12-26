from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User


class UserModelAdmin(BaseUserAdmin):
    
    # The fields to be used in displaying the User model.
    list_display = ["email", "name", "tc", "is_admin"]
    list_filter = ["is_admin"]

    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            "Create an Account",
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc", "is_admin", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserModelAdmin
admin.site.register(User, UserModelAdmin)
