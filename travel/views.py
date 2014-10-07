from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Trip


def home(request):
    return render(request, "travel/public/home.html")


def trips(request, user):
    user = User.objects.get(username=user)
    trips = Trip.get_active_trips(user=user)
    return render(request, "travel/public/trips.html", {
        "trips": trips,
        "user": user,
    })
