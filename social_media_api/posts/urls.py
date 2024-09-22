from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView
from .views import UserFeedView


# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet)  # Register post routes
router.register(r'comments', CommentViewSet)  # Register comment routes

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]

