from django.db import models
from django.contrib.auth.models import User
import datetime as dt
import pytz


class Trip(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    reason = models.TextField()

    def get_active_legs(self, **filters):
        now = dt.datetime.utcnow()
        return self.legs.filter(
            arrival_time__gte=now,
            departure_time__lte=now,
            **filters
        ).distinct()

    @classmethod
    def get_active_trips(cls, **filters):
        now = dt.datetime.utcnow()
        delta = dt.timedelta(weeks=1)
        return Trip.objects.filter(
            legs__departure_time__lte=(now + delta),
            legs__arrival_time__gte=(now - delta),
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


class Place(models.Model):
    name = models.CharField(max_length=128)
    photo = models.URLField()

    def __str__(self):
        return "<Place: {}>".format(self.name)


LODGING_TYPES = (
    ('hotel', 'Hotel'),
    ('house', 'House'),
)


class Lodging(models.Model):
    name = models.CharField(max_length=128)
    rewards_account = models.CharField(max_length=128)
    website = models.URLField()
    phone_number = models.CharField(max_length=32)
    lat = models.CharField(max_length=128)
    lon = models.CharField(max_length=128)
    address = models.TextField(max_length=128)
    place = models.ForeignKey(Place, related_name="lodgings")
    time_zone = models.CharField(max_length=100, choices=TIMEZONES)
    type = models.CharField(max_length=16, choices=LODGING_TYPES)

    def __str__(self):
        return "<Lodging: {}>".format(self.name)


class Stay(models.Model):
    lodging = models.ForeignKey(Lodging, related_name="stays")
    checkout_time = models.DateTimeField()
    checkin_time = models.DateTimeField()
    trip = models.ForeignKey(Trip, related_name="stays")
    user = models.ForeignKey(User)

    @property
    def complete(self, **filters):
        now = dt.datetime.now(dt.timezone.utc)
        return now >= self.checkout_time

    @property
    def checkin(self):
        return self.checkin_time.astimezone(
            pytz.timezone(self.lodging.time_zone))

    @property
    def checkout(self):
        return self.checkout_time.astimezone(
            pytz.timezone(self.lodging.time_zone))

    @classmethod
    def active_stays(cls, **filters):
        now = dt.datetime.utcnow()
        return Stay.objects.filter(
            checkin_time__lte=now,
            checkout_time__gte=now,
            **filters
        ).distinct()

    def __str__(self):
        return "<Stay: {} at {}>".format(self.checkin, self.lodging.name)


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
    def active(self):
        now = dt.datetime.now(dt.timezone.utc)
        return (now <= self.arrival_time and now >= self.departure_time)

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
