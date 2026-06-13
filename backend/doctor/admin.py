from django.contrib import admin
from django.utils.html import format_html
from .models import DoctorProfile, Qualification

class QualificationInline(admin.TabularInline):
    model = Qualification
    extra = 1
    fields = ["degree", "institution_bn", "institution_en", "year", "order"]

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    inlines = [QualificationInline]
    list_display = ["name_en", "speciality_en", "phone", "experience_years", "photo_preview"]
    readonly_fields = ["photo_preview"]

    def photo_preview(self, obj):
        if obj.photo:
            return format_html("<img src='{}' style='width:60px;height:60px;border-radius:50%;object-fit:cover;'>", obj.photo.url)
        return "ছবি নেই"
    photo_preview.short_description = "ছবি"
