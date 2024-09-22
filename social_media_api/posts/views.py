from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import PostSerializer
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# Importing the CustomUser model
User = get_user_model()

# Custom pagination class
class PostPagination(PageNumberPagination):
    page_size = 10  # Limit to 10 posts per page
    
# Viewset for Post: Handles all CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Fetch all posts
    serializer_class = PostSerializer  # Define which serializer to use
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users
    pagination_class = PostPagination  # Enable pagination
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_fields = ['title', 'content']  # Allow filtering by title or content

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author to the current user when creating a post

# Viewset for Comment: Handles all CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Fetch all comments
    serializer_class = CommentSerializer  # Define which serializer to use
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author to the current user when creating a comment
        

# View to generate a feed based on the users the current user follows
class UserFeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access the feed

    def get(self, request, *args, **kwargs):
        # Get the users the current user is following
        following_users = request.user.following.all()

        # Filter posts by the authors the current user follows and order them by creation date (newest first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts to return them as JSON
        serializer = PostSerializer(posts, many=True)

        # Return the serialized posts as the feed response
        return Response(serializer.data, status=200)

# Like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can like/unlike posts

    def post(self, request, pk):
        # Use get_object_or_404 to retrieve the post
        post = generics.get_object_or_404(Post, pk=pk)

        # Use get_or_create to ensure a like is only created once
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'error': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post owner
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.pk,
        )

        return Response({'message': 'Post liked successfully'}, status=status.HTTP_200_OK)

# Unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can like/unlike posts

    def post(self, request, pk):
        # Use get_object_or_404 to retrieve the post
        post = generics.get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({'error': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()

        return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)
