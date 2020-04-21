import datetime as dt

from django.db.models import Min, Max, Q

from rest_framework import generics

from scrappers.models import Event, Price
from scrappers.serializers import EventSerializer


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all(
        ).annotate(
            min_price=Min('prices__min_price')
        ).annotate(
            max_price=Max('prices__max_price')
        )
        params = self.request.query_params.keys()

        if 'price' in params:
            price = self.request.query_params['price']
            condition = Q(min_price__lte=price) & Q(max_price__gte=price)
            queryset = queryset.filter(condition)

        if 'name' in params:
            name = self.request.query_params['name']
            queryset = queryset.filter(name__icontains=name)

        if 'promoter_name' in params:
            promoter_name = self.request.query_params['promoter_name']
            queryset = queryset.filter(promoter_name__icontains=promoter_name)

        if 'start_date' in params:
            start_date = self.request.query_params['start_date']
            start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
            queryset = queryset.filter(start_date__range=(start_date, start_date + dt.timedelta(days=1)))

        return queryset


class EventUpdate(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def update_prices(self, data):
        event = Event.objects.get(id=data.get('id'))
        for price in data.get('prices'):
            price_obj, _ = Price.objects.get_or_create(event=event, price_type=price.get('price_type'))
            price_obj.min_price = price.get('min_price') or price_obj.min_price
            price_obj.max_price = price.get('max_price') or price_obj.max_price
            price_obj.currency = price.get('currency') or price_obj.currency
            price_obj.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code==200 and 'prices' in request.data:
            EventSerializer.validate_prices(request.data)
            self.update_prices(request.data)

        return response
