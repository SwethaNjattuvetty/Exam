from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError


def create_user(request):
    try:
        # Check if user with the same username already exists
        if not User.objects.filter(username="newuser").exists():
            user = User.objects.create(username="newuser", password="password")
            return HttpResponse(f"User {user.username} created!")
        else:
            return HttpResponse("User with this username already exists.")

    except IntegrityError as e:
        return HttpResponse(f"Error: {e}")


