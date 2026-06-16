from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer

class DoctorProfileView(RetrieveAPIView):
    serializer_class = DoctorProfileSerializer

    def get_object(self):
        # সবসময় প্রথম/একমাত্র প্রোফাইল রিটার্ন করবে
        return DoctorProfile.objects.prefetch_related('qualifications').first()