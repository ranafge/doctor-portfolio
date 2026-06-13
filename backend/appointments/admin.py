from django.contrib import admin
from django.utils.html import format_html
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "chamber", "preferred_date", "preferred_time", "colored_status", "created_at"]
    list_filter = ["status", "chamber", "preferred_date"]
    search_fields = ["name", "phone", "email"]
    
    ordering = ["-created_at"]
    readonly_fields = ["created_at"]

    fieldsets = (
        ("রোগীর তথ্য", {
            "fields": ("name", "phone", "email", "age", "problem")
        }),
        ("অ্যাপয়েন্টমেন্ট তথ্য", {
            "fields": ("chamber", "preferred_date", "preferred_time", "status")
        }),
        ("সিস্টেম তথ্য", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )

    def colored_status(self, obj):
        colors = {
            "pending": "#f59e0b",
            "confirmed": "#10b981",
            "cancelled": "#ef4444",
        }
        labels = {
            "pending": "অপেক্ষমান",
            "confirmed": "নিশ্চিত",
            "cancelled": "বাতিল",
        }
        color = colors.get(obj.status, "#888")
        label = labels.get(obj.status, obj.status)
        return format_html(
            "<span style='background:{};color:#fff;padding:3px 10px;border-radius:12px;font-size:0.8rem;font-weight:600;'>{}</span>",
            color, label
        )
    colored_status.short_description = "অবস্থা"
