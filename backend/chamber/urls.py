from django.urls import path
from .views import ChamberListView

urlpatterns = [
    path("", ChamberListView.as_view(), name="chambers"),
]
