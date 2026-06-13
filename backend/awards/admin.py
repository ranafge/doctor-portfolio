from django.contrib import admin
from .models import Award

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ["title_en", "organization_en", "year"]
    list_filter = ["year"]
    search_fields = ["title_bn", "title_en"]
    ordering = ["order"]
