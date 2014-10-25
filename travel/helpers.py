from django.http import HttpResponse
from django.views.generic import View
from restless.models import serialize

import datetime as dt
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, dt.timedelta):
            return obj.total_seconds()
        if isinstance(obj, (dt.date, dt.datetime)):
            if obj.tzinfo is None:
                raise TypeError(
                    "date '%s' is not fully timezone qualified." % (obj))
            return "{}".format(obj.isoformat())
        return super(JSONEncoder, self).default(obj, **kwargs)




class TravelView(View):
    http_method_names = ['get']  # HEAD soon?
    PUBLIC_SCHEMA = {}

    def lookup(self, *args, **kwargs):
        raise NotImplementedError("`lookup` method not implemented")

    def render(self, *args, **kwargs):
        raise NotImplementedError("`render` method not implemented")

    def get(self, request, *args, **kwargs):
        if request.META['HTTP_ACCEPT'].startswith("application/json"):
            return HttpResponse(json.dumps(serialize(
                    self.lookup(*args, **kwargs), **self.PUBLIC_SCHEMA),
                cls=JSONEncoder))
        return self.render(request, self.lookup(*args, **kwargs))
