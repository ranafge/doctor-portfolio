from rest_framework.generics import ListAPIView
from .models import Publication
from .serializers import PublicationSerializer

class PublicationListView(ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
