from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from jalali_date.admin import ModelAdminJalaliMixin



from .forms import UserCreationForm, UserChangeForm
from .models import MyUser, OtpCode


@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["first_name","last_name", "phone_number", "is_active", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["first_name", "last_name", "phone_number" , "password"]}),
        ("Permissions", {"fields": ["is_admin","is_active", "last_login"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["first_name", "last_name", "phone_number", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["first_name", "last_name"]
    ordering = ["first_name", "last_name"]
    filter_horizontal = []



@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'code', 'date_time_created']