from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title_en", "category_en", "date", "read_time"]
    list_filter = ["category_en", "date"]
    search_fields = ["title_bn", "title_en"]
    ordering = ["-date"]
