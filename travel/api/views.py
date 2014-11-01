from django.core.paginator import Paginator, EmptyPage

from django.http import HttpResponse
from django.views.generic import View
from restless.models import serialize
from restless.http import Http200

from django.contrib.auth.models import User
from ..models import Trip, Place, Stay
from .specs import TRIP_SPEC, PLACE_SPEC, STAY_SPEC

import datetime as dt
import math
import json



class APIListView(View):
    http_method_names = ['get']  # HEAD soon?
    PUBLIC_SCHEMA = {}
    max_per_page = 100

    def paginate(self, data, page, per_page):
        paginator = Paginator(data, per_page=per_page)
        return paginator.page(page)

    def filter(self, data, **params):
        return data

    def get(self, request, *args, **kwargs):
        params = dict(request.GET)
        data = self.get_query_set(request, *args, **kwargs)
        data = self.filter(data, **params)

        page = int(params.pop('page', 1))
        per_page = min(self.max_per_page, int(params.pop(
            'per_page', self.max_per_page)))

        try:
            data_page = self.paginate(data, page, per_page)
        except EmptyPage:
            raise HttpError(404, 'No such page (heh, literally - its out of bounds)')

        count = data_page.paginator.count
        response = [serialize(x, **self.PUBLIC_SCHEMA)
                    for x in data_page.object_list]

        response = Http200(response)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class APIDetailView(View):
    http_method_names = ['get']  # HEAD soon?
    PUBLIC_SCHEMA = None

    def get(self, request, *args, **kwargs):
        params = dict(request.GET)
        response = Http200(serialize(
            self.get_object(request, *args, **kwargs),
            **self.PUBLIC_SCHEMA))

        response['Access-Control-Allow-Origin'] = "*"
        return response


class TripsView(APIListView):
    PUBLIC_SCHEMA = TRIP_SPEC
    def get_query_set(self, request, user):
        user = User.objects.filter(username=user)
        trips = Trip.objects.filter(user=user)
        return trips


class StaysView(APIListView):
    PUBLIC_SCHEMA = STAY_SPEC
    def get_query_set(self, request, user):
        user = User.objects.filter(username=user)
        stays = Stay.objects.filter(user=user)
        return stays


class LocateView(APIDetailView):
    PUBLIC_SCHEMA = PLACE_SPEC

    def get_object(self, request, user):
        user = User.objects.filter(username=user)
        return Place.locate_user(user)
