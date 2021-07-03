from .utils import get_data_from_alphavantage,save_latest_rate_to_db
from coinmena.celery import app

#task to perform the price fetching from Alphavantage
#celery beat is used to schedule the task every hour
@app.task
def refresh_task():
    get_data_from_alphavantage('BTC','USD')
