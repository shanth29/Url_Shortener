import string
from random import choices
from . models import Urls
import re
import datetime
from datetime import timedelta
from django.utils.timezone import utc


def create_short_url(link_data):
    if Urls.objects.filter(long_url = link_data):
        return True
    else:
        url_data = string.digits + string.ascii_letters
        while True:
            short_url = ''.join(choices(url_data, k = 7))
            if Urls.objects.filter(short_url = short_url):
                continue
            else:
                Urls.objects.create(long_url = link_data, short_url = short_url, total_hits = 1)
                break
        return False


def fetch_long_url(link_data):
    raw_data = link_data.split('/')
    short_url = raw_data[-1]
    if Urls.objects.filter(short_url = short_url):
        return short_url
    else:
        return False


def get_similar_data(data):
    store_data = []
    value = Urls.objects.all().values_list('long_url')
    for i in range(len(value)):
        if data in str(value[i]).replace("('","").replace("',)",""):
            store_data.append(str(value[i]).replace("('","").replace("',)",""))
        else:
            pass
    return store_data


def calculate_time(data):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    get_date = Urls.objects.get(short_url = data)
    get_date = get_date.created_at
    timediff = now - get_date
    return (str(timediff).split(':')[0])
    