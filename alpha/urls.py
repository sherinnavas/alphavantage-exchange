from django.urls import path
from alpha.views import FetchExchangeRate

urlpatterns = [
    path('v1/qoutes', FetchExchangeRate.as_view(),name='fetch_exchange_rate'),
]
