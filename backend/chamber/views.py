from rest_framework.generics import ListAPIView
from .models import Chamber
from .serializers import ChamberSerializer

class ChamberListView(ListAPIView):
    queryset = Chamber.objects.all()
    serializer_class = ChamberSerializer
