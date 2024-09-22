from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from rest_framework import generics, status

# View to get the notifications for the authenticated user
class NotificationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can see their notifications

    def get(self, request):
        # Get all notifications for the current user
        notifications = Notification.objects.filter(recipient=request.user)

        # Mark all notifications as read
        notifications.update(read=True)

        # Return a list of notifications
        notifications_data = [
            {
                'actor': notification.actor.username,
                'verb': notification.verb,
                'target': str(notification.target),
                'timestamp': notification.timestamp,
                'read': notification.read
            }
            for notification in notifications
        ]
        return Response(notifications_data, status=status.HTTP_200_OK)
