from rest_framework.generics import ListAPIView
from .models import Video, Photo
from .serializers import VideoSerializer, PhotoSerializer

class VideoListView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class PhotoListView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
