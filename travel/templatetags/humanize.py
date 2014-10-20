from django import template

import datetime as dt
import humanize

register = template.Library()


@register.filter(name='humanize_delta')
def humanize_delta(value):
    return humanize.naturaltime(
        dt.datetime.now(dt.timezone.utc) - value)


@register.filter(name='humanize_date')
def humanize_delta(value):
    return dt.datetime.strftime(value, "%A, %b %d, %Y, %I:%M %p %Z")
