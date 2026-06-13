from rest_framework import serializers
from .models import Appointment
import re

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["status", "created_at"]
        extra_kwargs = {
            "email": {"required": False, "allow_blank": True}
        }

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("নাম আবশ্যক।")
        if len(value) < 2:
            raise serializers.ValidationError("নাম কমপক্ষে ২ অক্ষরের হতে হবে।")
        if len(value) > 100:
            raise serializers.ValidationError("নাম ১০০ অক্ষরের বেশি হবে না।")
        # শুধু বাংলা, ইংরেজি অক্ষর ও স্পেস
        if not re.match(r"^[a-zA-Zঀ-৿\s]+$", value):
            raise serializers.ValidationError("নামে শুধু বাংলা বা ইংরেজি অক্ষর ব্যবহার করুন।")
        return value

    def validate_phone(self, value):
        value = value.strip()
        if not re.match(r"^[0-9]{11}$", value):
            raise serializers.ValidationError("১১ সংখ্যার ফোন নম্বর দিন।")
        if not value.startswith("01"):
            raise serializers.ValidationError("বাংলাদেশি মোবাইল নম্বর দিন (01 দিয়ে শুরু)।")
        return value

    def validate_age(self, value):
        if value < 0 or value > 120:
            raise serializers.ValidationError("বয়স ০ থেকে ১২০ এর মধ্যে হতে হবে।")
        return value

    def validate_email(self, value):
        if value and not re.match(r"^[^@]+@[^@]+\.[^@]+$", value):
            raise serializers.ValidationError("সঠিক ইমেইল ঠিকানা দিন।")
        return value

    def validate_problem(self, value):
        value = value.strip()
        if len(value) < 10:
            raise serializers.ValidationError("সমস্যার বিবরণ কমপক্ষে ১০ অক্ষরের হতে হবে।")
        if len(value) > 1000:
            raise serializers.ValidationError("সমস্যার বিবরণ ১০০০ অক্ষরের বেশি হবে না।")
        return value

    def validate_preferred_date(self, value):
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("অতীতের তারিখ দেওয়া যাবে না।")
        return value
