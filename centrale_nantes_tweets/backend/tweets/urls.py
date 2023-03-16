from django.urls import path
from .views import LatestPosts

urlpatterns = [
    path("api/posts/", LatestPosts.as_view(), name="latest_posts"),
]
