from django.urls import path
from .views import VideoListView, PhotoListView

urlpatterns = [
    path("videos/", VideoListView.as_view(), name="videos"),
    path("photos/", PhotoListView.as_view(), name="photos"),
]
