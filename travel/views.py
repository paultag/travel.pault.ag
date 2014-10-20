from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

from django.contrib.auth.models import User
from .models import Trip


def home(request):
    return render(request, "travel/public/home.html")


@login_required
def trips(request, user):
    user = User.objects.get(username=user)
    active_trips = Trip.active_trips(user=user)
    return render(request, "travel/public/trips.html", {
        "active_trips": active_trips,
        "user": user,
    })


@login_required
def trip(request, trip):
    trip = Trip.objects.get(id=trip)
    legs = trip.legs.all().order_by("departure_time")

    return render(request, "travel/public/trip.html", {
        "trip": trip,
        "legs": legs,
        "user": trip.user,
        "settings": settings,
    })
