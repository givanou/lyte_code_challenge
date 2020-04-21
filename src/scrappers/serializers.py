import datetime as dt

from rest_framework import serializers
from .models import Event, Price


class PriceSrializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['currency', 'price_type', 'max_price', 'min_price']


class EventSerializer(serializers.ModelSerializer):
    prices = PriceSrializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'url', 'start_date', 'end_date', 'promoter_name', 'prices' ]

    def __validate_datetimes(self, data, event):
        start_date = data.get('start_date') or event.start_date
        end_date = data.get('end_date') or event.end_date

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("Finish must occur after start")

    @staticmethod
    def validate_prices(data):
        event = Event.objects.get(id=data.get('id'))
        for price in data.get('prices', []):
            price = PriceSrializer().validate(price)
            min_price = price.get('min_price')
            max_price = price.get('max_price')
            price_type = price.get('price_type')
            try:
                price_obj = Price.objects.get(event=event, price_type=price_type)
                min_price = min_price or price_obj.min_price
                max_price = max_price or price_obj.max_price
            except Price.DoesNotExist:
                pass

            if min_price and float(min_price) < 0:
                raise serializers.ValidationError("Price should be positive decimal number!")
            if max_price and float(max_price) < 0:
                raise serializers.ValidationError("Price should be positive decimal number!")

            if min_price and max_price and float(min_price) > float(max_price):
                raise serializers.ValidationError("Min Price should not be greater than max price!")

    def validate(self, data):
        data = super().validate(data)
        event = Event.objects.get(id=data.get('id'))
        self.__validate_datetimes(data, event)
        return data
