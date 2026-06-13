from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title_en", "source", "date"]
    list_filter = ["source", "date"]
    search_fields = ["title_bn", "title_en"]
    ordering = ["-date"]
