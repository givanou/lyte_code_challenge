from django.db import models


class Event(models.Model):
    id = models.CharField(primary_key=True, max_length=100, verbose_name='Ticketmaster id')
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    url = models.URLField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    promoter_name = models.TextField(null=True)


class Price(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='prices')
    price_type = models.CharField(max_length=100)
    currency = models.CharField(max_length=20)
    max_price = models.DecimalField(decimal_places=2, null=True, max_digits=7)
    min_price = models.DecimalField(decimal_places=2, null=True, max_digits=7)
