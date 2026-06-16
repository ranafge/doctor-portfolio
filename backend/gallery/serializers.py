from rest_framework import serializers
from .models import Video, Photo
from rest_framework import serializers
from .models import Video, Photo

class VideoSerializer(serializers.ModelSerializer):
    embed_url = serializers.ReadOnlyField()
    
    class Meta:
        model = Video
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()  
    
    class Meta:
        model = Photo
        fields = "__all__"
    
    def get_image(self, obj): 
        if hasattr(obj, 'image') and obj.image:
            if hasattr(obj.image, 'url'):
                return obj.image.url
            else:
                return str(obj.image)
        return None