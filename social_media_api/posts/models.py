from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

# Post model: Represents a social media post
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the User model
    title = models.CharField(max_length=100)  # Post title
    content = models.TextField()  # Post content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on changes

    def __str__(self):
        return self.title  # Show title as string representation


# Comment model: Represents comments on posts
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Link to the Post model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the User model
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on changes

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

# Get the user model
User = get_user_model()

class Like(models.Model):
    # ForeignKey to the User who liked the post
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # ForeignKey to the liked Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    
    # Timestamp for when the like was created
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure a user can like a post only once
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'
