from django.contrib import admin
from .models import BannedApp


@admin.register(BannedApp)
class BannedAppAdmin(admin.ModelAdmin):
    list_display = ("app_name", "country_name", "is_active", "ban_date")
