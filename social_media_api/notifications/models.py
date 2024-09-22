# notifications/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Get the user model
User = get_user_model()

class Notification(models.Model):
    # The recipient of the notification
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    
    # The actor (the user who triggered the notification)
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor')
    
    # Verb describing the action (e.g., "liked", "followed")
    verb = models.CharField(max_length=255)
    
    # The target object (could be a post, comment, or other objects)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    
    # Timestamp for when the notification was created
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Whether the notification has been read
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.recipient.username}: {self.verb} by {self.actor.username}'

    class Meta:
        # Ensure notifications are ordered by timestamp
        ordering = ['-timestamp']