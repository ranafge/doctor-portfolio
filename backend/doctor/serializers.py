from rest_framework import serializers

from .models import DoctorProfile, Qualification

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['id', 'degree', 'institution_bn', 'institution_en', 'year']

class DoctorProfileSerializer(serializers.ModelSerializer):
    qualifications = QualificationSerializer(many=True, read_only=True)

    class Meta:
        model = DoctorProfile
        fields = '__all__'