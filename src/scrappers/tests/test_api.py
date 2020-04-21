import datetime as dt
import json
import pytz

from django.test import TestCase
from django.utils.timezone import make_aware

from scrappers.models import Event, Price


class TestListEndpoint(TestCase):
    def setUp(self):
        start_date_artist = make_aware(dt.datetime(2020, 10, 10))
        start_date_match = make_aware(dt.datetime(2020, 10, 10))
        start_date_show = make_aware(dt.datetime(2021, 11, 11))
        event_artist = Event(
            name='Artist 1',
            id='1',
            promoter_name='p1',
            start_date=start_date_artist
        )
        event_match = Event(
            name='Match 2',
            id='2',
            promoter_name='p2',
            start_date=start_date_match
        )
        event_show = Event(
            name='Artist Show 3',
            id='3',
            promoter_name='p3',
            start_date=start_date_show
        )
        event_artist.save()
        event_match.save()
        event_show.save()

        price_artist = Price(
            event=event_artist,
            price_type='standart',
            currency='USD',
            min_price=48.0,
            max_price=90.0
        )
        price_match = Price(
            event=event_match,
            price_type='standart',
            currency='USD',
            min_price=10.0,
            max_price=60.0
        )
        price_show = Price(
            event=event_show,
            price_type='standart',
            currency='USD',
            min_price=70.0,
            max_price=190.0
        )
        price_artist.save()
        price_match.save()
        price_show.save()

    def test_name_filtering(self):
        response = self.client.get('/events', {'name': 'artist'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 2)

    def test_price_filtering(self):
        response = self.client.get('/events', {'price': '48'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 2)

        response = self.client.get('/events', {'price': '180'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 1)

        response = self.client.get('/events', {'price': '400'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 0)

    def test_promoter_name_filtering(self):
        response = self.client.get('/events', {'promoter_name': 'p2'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['name'], 'Match 2')

    def test_start_date_filtering(self):
        response = self.client.get('/events', {'start_date': '2020-10-10'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 2)

        response = self.client.get('/events', {'start_date': '2021-11-11'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 1)

        response = self.client.get('/events', {'start_date': '2021-01-01'})
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 0)


class TestUpdateEndpoint(TestCase):
    def setUp(self):
        start_date_artist = make_aware(dt.datetime(2020, 10, 10))
        event_artist = Event(
            name='Artist 1',
            id='1',
            promoter_name='p1',
            start_date=start_date_artist
        )
        event_artist.save()
        price_artist = Price(
            event=event_artist,
            price_type='standard',
            currency='USD',
            min_price=48.0,
            max_price=90.0
        )
        price_artist.save()

    def test_put(self):
        data = json.loads(
            """{
                "id": "1",
                "name": "Hamilton (Touring)",
                "description": null,
                "url": "https://www.ticketmaster.com/hamilton-touring-los-angeles-california-11-13-2020/event/someurl",
                "start_date": "2020-11-14T04:00:00Z",
                "end_date": null,
                "promoter_name": "BROADWAY IN HOLLYWOOD",
                "prices": [
                    {
                        "currency": "USD",
                        "price_type": "standard",
                        "max_price": "475.00",
                        "min_price": "55.00"
                    }
                ]
            }
            """
        )
        response = self.client.put('/update/1',content_type='application/json', data=data)
        event = Event.objects.get(id='1')
        self.assertEqual(event.name, "Hamilton (Touring)")
        self.assertEqual(
            event.url,
            "https://www.ticketmaster.com/hamilton-touring-los-angeles-california-11-13-2020/event/someurl"
        )
        price = event.prices.get(price_type='standard')
        self.assertEqual(price.max_price, 475.0)
        self.assertEqual(price.min_price, 55.0)

    def test_price_negative_value(self):
        data = json.loads(
            """{
                "id": "1",
                "name": "Hamilton (Touring)",
                "description": null,
                "url": "https://www.ticketmaster.com/hamilton-touring-los-angeles-california-11-13-2020/event/someurl",
                "start_date": "2020-11-14T04:00:00Z",
                "end_date": null,
                "promoter_name": "BROADWAY IN HOLLYWOOD",
                "prices": [
                    {
                        "currency": "USD",
                        "price_type": "standard",
                        "max_price": "475.00",
                        "min_price": "-55.00"
                    }
                ]
            }
            """
        )
        response = self.client.put('/update/1', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'["Price should be positive decimal number!"]')

    def test_min_max_price_value(self):
        data = json.loads(
            """{
                "id": "1",
                "name": "Hamilton (Touring)",
                "description": null,
                "url": "https://www.ticketmaster.com/hamilton-touring-los-angeles-california-11-13-2020/event/someurl",
                "start_date": "2020-11-14T04:00:00Z",
                "end_date": null,
                "promoter_name": "BROADWAY IN HOLLYWOOD",
                "prices": [
                    {
                        "currency": "USD",
                        "price_type": "standard",
                        "max_price": "25.00",
                        "min_price": "55.00"
                    }
                ]
            }
            """
        )
        response = self.client.put('/update/1', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'["Min Price should not be greater than max price!"]')

    def test_patch(self):
        data = json.loads(
            """{
                "id": "1",
                "name": "New Name"
            }
            """
        )
        response = self.client.patch('/update/1', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 200)
        event = Event.objects.get(id='1')
        self.assertEqual(event.name, 'New Name')
