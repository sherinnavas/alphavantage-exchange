from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from alpha.models import Currency,Exchange
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from alpha.utils import get_data_from_alphavantage
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class FetchExchangeRate(View):
    #Fetch the latest exchange rate data from the database
    def get(self,request):
        latest_rate_from_db = Exchange.objects.latest('fetched')
        data = {
        'from_currency':latest_rate_from_db.from_currency.code,
        'to_currency':latest_rate_from_db.to_currency.code,
        'exchange_rate':latest_rate_from_db.exchange_rate,
        'fetched_timestamp':latest_rate_from_db.fetched
        }
        response = {
        'success': True,
        'code': 200,
        'message': "Successfully fetched latest data from database",
        'data':data
        }
        return JsonResponse(response)

    #Fetch the exchange data from Alphavantage Api, and save it to the database
    def post(self, request):
        #function call to fetch data from Alphavantage api and save to database
        latest_saved,message = get_data_from_alphavantage('BTC','USD')
        if latest_saved:
            data = {
            'from_currency':latest_saved.from_currency.code,
            'to_currency':latest_saved.to_currency.code,
            'exchange_rate':latest_saved.exchange_rate,
            'fetched_timestamp':latest_saved.fetched
            }
            response = {
            'success': True,
            'code': 200,
            'message': message,
            'data':data
            }
        else:
            response = {
                'success': False,
                'code': 400,
                'message': message,
            }
        return JsonResponse(response)
