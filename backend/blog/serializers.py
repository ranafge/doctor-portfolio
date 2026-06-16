from rest_framework import serializers
from .models import BlogPost

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()  
    class Meta:
        model = BlogPost
        fields = "__all__"
    
    def get_image(self, obj): 
        if hasattr(obj, 'image') and obj.image:
            if hasattr(obj.image, 'url'):
                return obj.image.url
            else:
                return str(obj.image)
        return None