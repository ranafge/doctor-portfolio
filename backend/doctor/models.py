from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField  # এই লাইনটা যোগ করো


class DoctorProfile(models.Model):
    name_bn = models.CharField(max_length=200, verbose_name="নাম (বাংলা)")
    name_en = models.CharField(max_length=200, verbose_name="নাম (ইংরেজি)")
    title_bn = models.CharField(max_length=300, verbose_name="পদবি (বাংলা)")
    title_en = models.CharField(max_length=300, verbose_name="পদবি (ইংরেজি)")
    speciality_bn = models.CharField(max_length=200)
    speciality_en = models.CharField(max_length=200)
    hospital_bn = models.CharField(max_length=300)
    hospital_en = models.CharField(max_length=300)
    address_bn = models.TextField()
    address_en = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    patients_count = models.PositiveIntegerField(default=0)
    publications_count = models.PositiveIntegerField(default=0)
    # photo = models.ImageField(upload_to='doctor/', blank=True, null=True)
    photo = CloudinaryField('image', blank=True, null=True)


    def __str__(self):
        return self.name_en

class Qualification(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='qualifications')
    degree = models.CharField(max_length=100)
    institution_bn = models.CharField(max_length=200)
    institution_en = models.CharField(max_length=200)
    year = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} - {self.institution_en}"