from django.contrib import admin

from apps.users.models import Financials, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "identificator",
        "birth_date",
        "age",
    ]
    readonly_fields = [
        "identificator",
        "age",
    ]


@admin.register(Financials)
class FinancialsAdmin(admin.ModelAdmin):
    list_display = [
        "profile",
        "salary",
        "hourly_pay",
        "extra_hourly_pay",
        "is_student",
    ]
