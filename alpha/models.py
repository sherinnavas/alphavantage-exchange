from django.db import models

# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class Exchange(models.Model):
    from_currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name="From",null=True)
    to_currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name="To",null=True)
    exchange_rate = models.FloatField("Exchange Rate",null=True)
    ask_price = models.FloatField("Ask Price",null=True)
    bid_price = models.FloatField("Bid price",null=True)
    fetched = models.DateTimeField("Fetched Timestamp(UTC)",null=True)

    def __str__(self):
        return str(self.exchange_rate)
