from django.contrib import admin
from .models import Chamber

@admin.register(Chamber)
class ChamberAdmin(admin.ModelAdmin):
    list_display = ["name_en", "phone", "time_en", "days_en", "order"]
    ordering = ["order"]
