from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    user = models.ForeignKey(User)
    reason = models.TextField()


class ServiceProvider(models.Model):
    name = models.TextField()
    rewards_account = models.TextField()
    website = models.TextField()
    phone_number = models.TextField()


class Flight(models.Model):
    user = models.ForeignKey(User)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    carrier = models.ForeignKey(ServiceProvider)
    trip = models.ForeignKey(Trip, related_name="flights")
