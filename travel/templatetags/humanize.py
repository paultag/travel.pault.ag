from django import template

import datetime as dt
import humanize

register = template.Library()


@register.filter(name='humanize_delta')
def humanize_delta(value):
    return humanize.naturaltime(
        dt.datetime.now(dt.timezone.utc) - value)
