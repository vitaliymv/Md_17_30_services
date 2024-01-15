from datetime import datetime
from datetime import timedelta
from django import template

from core.services import get_total_duration

register = template.Library()


@register.filter()
def format_date(date_str):
    date = datetime.strptime(
        date_str, "%Y-%m-%d"
    )
    return date.strftime("%B %d, %Y")


@register.filter()
def get_duration(date_str):
    date = datetime.strptime(
        date_str, "%Y-%m-%d"
    )
    start = datetime(date.year, date.month, date.day)
    end = start + timedelta(hours=23, minutes=59)
    start = start.isoformat() + ".000"
    end = end.isoformat() + ".000"
    seconds = get_total_duration(start, end)
    return timedelta(seconds=seconds)
