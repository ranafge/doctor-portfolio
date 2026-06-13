from django.contrib import admin
from django.utils.html import format_html
from .models import Video, Photo

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title_en", "category_en", "duration", "views", "is_featured", "order"]
    list_filter = ["category_en", "is_featured"]
    list_editable = ["is_featured", "order"]
    search_fields = ["title_bn", "title_en"]
    ordering = ["order"]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title_en", "category", "date", "order", "photo_preview"]
    list_filter = ["category"]
    ordering = ["order"]

    def photo_preview(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' style='width:60px;height:60px;object-fit:cover;border-radius:6px;'>",
                obj.image.url
            )
        return "ছবি নেই"
    photo_preview.short_description = "প্রিভিউ"
