from rest_framework import serializers
from .models import Video, Photo

class VideoSerializer(serializers.ModelSerializer):
    embed_url = serializers.ReadOnlyField()
    class Meta:
        model = Video
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
