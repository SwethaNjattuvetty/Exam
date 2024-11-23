from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Test Django signal"

    def handle(self, *args, **kwargs):
        print("Before creating user...")
        user = User.objects.create(username="testuser")
        print("After creating user...")
