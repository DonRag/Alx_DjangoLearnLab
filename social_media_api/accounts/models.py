# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Adds a bio field to allow users to describe themselves
    bio = models.TextField(blank=True, null=True)

    # Adds an image field for profile pictures (ensure you have Pillow installed)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # A Many-to-Many relationship with self to represent followers
    # symmetrical=False means a user following another user doesn't mean the reverse is true
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username  # Returns the username as the string representation of the user
