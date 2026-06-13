from rest_framework.generics import ListAPIView
from .models import Award
from .serializers import AwardSerializer

class AwardListView(ListAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
