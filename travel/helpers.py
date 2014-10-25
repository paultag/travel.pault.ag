from django.views.generic import View

from django.http import HttpResponse
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


def _wrap(data):
    return HttpResponse(json.dumps(data, cls=JSONEncoder))



def userview(fn):
    def _(*args, user, **kwargs):
        user = User.objects.get(username=user)
        return fn(*args, user=user, **kwargs)
    return _


class TravelView(View):
    http_method_names = ['get']  # HEAD soon?

    def lookup(self, *args, **kwargs):
        raise NotImplementedError("`lookup` method not implemented")

    def render(self, *args, **kwargs):
        raise NotImplementedError("`render` method not implemented")

    def get(self, request, *args, **kwargs):
        return self.render(request, self.lookup(*args, **kwargs))
