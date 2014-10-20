from django.db import models
from django.contrib.auth.models import User
import datetime as dt
import pytz


class Trip(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    reason = models.TextField()

    def active_legs(self, **filters):
        now = dt.datetime.utcnow()
        return self.legs.filter(
            arrival_time__gte=now,
            departure_time__lte=now,
            **filters
        ).distinct()

    @classmethod
    def active_trips(cls, **filters):
        now = dt.datetime.utcnow()
        return Trip.objects.filter(
            legs__arrival_time__gte=now,
            legs__departure_time__lte=now,
            **filters
        ).distinct()

    @property
    def start(self):
        return self.legs.order_by("departure_time").first().departure

    @property
    def end(self):
        return self.legs.order_by("-arrival_time").first().arrival

    def __str__(self):
        return "<Trip: {}>".format(self.name)


class ServiceProvider(models.Model):
    name = models.CharField(max_length=128)
    rewards_account = models.CharField(max_length=128)
    website = models.URLField()
    phone_number = models.CharField(max_length=32)

    def __str__(self):
        return "<ServiceProvider: {}>".format(self.name)

TIMEZONES = list(zip(pytz.all_timezones, pytz.all_timezones))


class Stop(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=16)
    lat = models.CharField(max_length=128)
    lon = models.CharField(max_length=128)
    time_zone = models.CharField(max_length=100, choices=TIMEZONES)

    def __str__(self):
        return "<Stop: {} ({})>".format(self.code, self.name)


LEG_TYPES = (
    ('air', 'Airplane'),
    ('train', 'Train'),
    ('bus', 'Bus'),
)


class Leg(models.Model):
    number = models.CharField(max_length=128)
    origin = models.ForeignKey(Stop, related_name="inbound_legs")
    destination = models.ForeignKey(Stop, related_name="outbound_legs")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    carrier = models.ForeignKey(ServiceProvider, related_name="legs")
    trip = models.ForeignKey(Trip, related_name="legs")
    type = models.CharField(max_length=16, choices=LEG_TYPES)

    @property
    def complete(self, **filters):
        now = dt.datetime.now(dt.timezone.utc)
        return now >= self.arrival_time

    @property
    def arrival(self):
        return self.arrival_time.astimezone(
            pytz.timezone(self.destination.time_zone))

    @property
    def departure(self):
        return self.departure_time.astimezone(
            pytz.timezone(self.origin.time_zone))

    @property
    def length(self):
        return self.arrival - self.departure

    @property
    def percent(self, **filters):
        now = dt.datetime.now(dt.timezone.utc)

        from_start = self.arrival_time - now
        from_end = now - self.departure_time

        total = from_start + from_end  # Total delta of the trip
        finished = (total - from_start)

        return ((finished.total_seconds() / total.total_seconds()) * 100)

    def __str__(self):
        return "<Leg: {} {} on {}>".format(
            self.carrier.name,
            self.number,
            self.departure_time
        )
