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

    def __str__(self):
        return "<ServiceProvider: {}>".format(self.name)


class Flight(models.Model):
    user = models.ForeignKey(User)
    departure_time = models.DateTimeField()
    flight_number = models.TextField()
    arrival_time = models.DateTimeField()
    carrier = models.ForeignKey(ServiceProvider)
    trip = models.ForeignKey(Trip, related_name="flights")
