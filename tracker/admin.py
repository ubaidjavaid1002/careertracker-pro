from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "company",
        "position",
        "status",
        "source",
        "applied_date"
    )

    list_filter = (
        "status",
        "source"
    )

    search_fields = (
        "company",
        "position"
    )