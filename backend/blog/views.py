from rest_framework.generics import ListAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
