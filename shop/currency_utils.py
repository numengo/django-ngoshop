import threading
from django.conf import settings
from ip_utils import IPu

#geo = IPu()


def get_currency_by_ip(ip=None):
    geo = IPu()
    continent = geo.get_client_continent(ip)
    country = geo.get_client_country(ip)
    if continent == 'EU':
        if country == 'GB':
            return 'GBP'
        else:
            return 'EUR'
    if country == 'BR':
        return 'BRL'
    return 'USD'


def set_currency(currency):
    setattr(threading.currentThread(), 'shop_currency', currency)


def get_currency():
    return getattr(threading.currentThread(), 'shop_currency', settings.SHOP_CURRENCIES[0][0])
