from django.contrib import admin
from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "journal", "year", "tag"]
    list_filter = ["year", "tag"]
    search_fields = ["title", "journal"]
    ordering = ["order"]
