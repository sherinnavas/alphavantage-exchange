from .models import Exchange
from datetime import datetime, timedelta
import time
import requests
from alpha.models import Currency,Exchange
from django.conf import settings

#saving the fetched data from api to the databse
def save_latest_rate_to_db(data,from_currency,to_currency):
    exchange_data = list(data.values())[0]
    details_list = list(exchange_data.values())

    exchange_rate = details_list[4]
    fetched = details_list[5]
    bid_price = details_list[7]
    ask_price = details_list[8]
    exchange_data = Exchange.objects.create(
        from_currency=from_currency,
        to_currency=to_currency,
        exchange_rate=exchange_rate,
        fetched=fetched,
        bid_price=bid_price,
        ask_price=ask_price
        )
    return exchange_data

#get the data from Alphavantage Api by passing from and to currencies
def get_data_from_alphavantage(from_currency,to_currency):
    api_key = settings.ALPHA_API_KEY
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}'.format(from_currency=from_currency,to_currency=to_currency,api_key=api_key)
    r = requests.get(url)
    data = r.json()
    if not 'Error Message' in data.keys():
        from_currency = Currency.objects.get(code=from_currency)
        to_currency =  Currency.objects.get(code=to_currency)
        latest_saved = save_latest_rate_to_db(data,from_currency,to_currency)
        message = "Exchange Rate Fetched & Saved to Database successfully!"
    else:
        latest_saved = None
        message = list(data.values())[0]
    return (latest_saved,message)
