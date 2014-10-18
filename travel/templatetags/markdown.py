from django import template

import datetime as dt
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_(value):
    return markdown.markdown(value)
