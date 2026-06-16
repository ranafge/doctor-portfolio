from django.db import models
from cloudinary.models import CloudinaryField  # ✅ এটা যোগ করো

class Video(models.Model):
    title_bn = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    description_bn = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    youtube_id = models.CharField(max_length=50)
    category_bn = models.CharField(max_length=100)
    category_en = models.CharField(max_length=100)
    duration = models.CharField(max_length=10, default="0:00")
    views = models.CharField(max_length=20, default="0")
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title_en

    @property
    def embed_url(self):
        return f"https://www.youtube.com/embed/{self.youtube_id}"


class Photo(models.Model):
    CATEGORY_CHOICES = [
        ("conference", "Conference"),
        ("award", "Award"),
        ("chamber", "Chamber"),
        ("other", "Other"),
    ]
    title_bn = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    date = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title_en