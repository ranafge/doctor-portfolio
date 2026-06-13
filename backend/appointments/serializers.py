from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["status", "created_at"]
        extra_kwargs = {"email": {"required": False, "allow_blank": True}}
