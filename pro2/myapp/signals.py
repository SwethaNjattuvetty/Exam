from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")
    if created:
        print(f"User {instance.username} was created!")
