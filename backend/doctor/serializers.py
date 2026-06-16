from rest_framework import serializers
from .models import DoctorProfile, Qualification

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['id', 'degree', 'institution_bn', 'institution_en', 'year']

class DoctorProfileSerializer(serializers.ModelSerializer):
    qualifications = QualificationSerializer(many=True, read_only=True)
    photo = serializers.SerializerMethodField()  # ✅ এটা যোগ করো

    class Meta:
        model = DoctorProfile
        fields = [
            'id',
            'name_bn',
            'name_en',
            'title_bn',
            'title_en',
            'speciality_bn',
            'speciality_en',
            'hospital_bn',
            'hospital_en',
            'address_bn',
            'address_en',
            'phone',
            'email',
            'experience_years',
            'patients_count',
            'publications_count',
            'photo',
            'qualifications'
        ]
    def get_photo(self, obj):
        if hasattr(obj, 'photo') and obj.photo:
            # Cloudinary URL
            if hasattr(obj.photo, 'url'):
                return obj.photo.url
            else:
                return str(obj.photo)
        return None