import datetime
import json
from urllib.request import urlopen
from urllib.parse import urlencode

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from scrappers.models import Event, Price


class Command(BaseCommand):
    help = 'Scrape data from the Ticketmaster'

    def add_arguments(self, parser):
        parser.add_argument(
            '--pages',
            action='store',
            type=int,
            default=settings.TICKETMASTER_API_PAGES
        )

        parser.add_argument(
            '--size',
            action='store',
            type=int,
            default=settings.TICKETMASTER_API_PAGE_SIZE
        )

    def __get_dates(self, dates):
        def get_date(key):
            info = dates.get(key)
            if not info:
                return
            raw_value = info.get('dateTime')
            if raw_value:
                value = datetime.datetime.strptime(raw_value, '%Y-%m-%dT%H:%M:%SZ')
                value = make_aware(value)
                return value

        start_date = get_date('start')
        end_date = get_date('end')

        return start_date, end_date

    def __init_event(self, item):
        new_event = Event()
        new_event.name = item.get('name')
        new_event.id = item.get('id')
        new_event.promoter_name = item.get('promoter', {}).get('name')
        new_event.url = item.get('url')
        new_event.description = item.get('description')
        start_date, end_date = self.__get_dates(item.get('dates'))
        new_event.start_date = start_date
        new_event.end_date = end_date
        return new_event

    def __init_prices(self, prices, event):
        result = []
        for price in prices:
            price['id'] = event.id
            result.append(price)
        return result

    def __process_prices(self, prices):
        result = []
        for price in prices:
            event = Event.objects.get(id=price['id'])
            new_price = Price(event=event)
            new_price.currency = price['currency']
            new_price.max_price = price['max']
            new_price.min_price = price['min']
            new_price.price_type = price['type']
            result.append(new_price)
        return result

    def get_data(self, pages, size):
        result = []
        for i in range(1, pages + 1):
            params = urlencode({
                'page': i,
                'size': size,
                'apikey': settings.TICKETMASTER_API_KEY
            })
            url = settings.TICKETMASTER_API_URL + '?' + params
            response = urlopen(url)
            if response.status == 200:
                raw_data = response.read()
                response_dict = json.loads(raw_data)
                result += response_dict.get('_embedded', {}).get('events')
        return result

    def store_data(self, items):
        current_ids = list(Event.objects.all().values_list('id', flat=True))
        events_to_save = []
        prices_to_process = []
        for item in items:
            if item.get('id') in current_ids:
                continue
            current_ids.append(item.get('id'))
            new_event = self.__init_event(item)
            events_to_save.append(new_event)
            prices_to_process += self.__init_prices(item.get('priceRanges', []), new_event)
        Event.objects.bulk_create(events_to_save)
        print('%s events were scrapped' % len(events_to_save))
        prices_to_save = self.__process_prices(prices_to_process)
        Price.objects.bulk_create(prices_to_save)
        print('%s prices were created' % len(prices_to_save))

    def handle(self, *args, **options):
        pages = options.get('pages')
        size = options.get('size')

        data = self.get_data(pages, size)
        self.store_data(data)
