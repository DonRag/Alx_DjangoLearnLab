from django.core.management.base import BaseCommand
from relationship_app.models import UserProfile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cleans up the UserProfile and User tables.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning up UserProfile table...")
        UserProfile.objects.all().delete()

        self.stdout.write("Cleaning up User table...")
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Cleanup completed successfully.'))
