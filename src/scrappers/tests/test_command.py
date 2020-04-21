from django.test import TestCase
from django.core.management import call_command

from unittest.mock import patch

from scrappers.models import Event, Price
from .mock_values import api_response_mock


# Create your tests here.

class TestCommand(TestCase):

    @patch('scrappers.management.commands.ticketmaster.urlopen', return_value=api_response_mock)
    def test_objects_created(self, urlopen_mock):
        self.assertEqual(Event.objects.count(), 0)
        self.assertEqual(Price.objects.count(), 0)
        call_command('ticketmaster', **{'pages': 1})
        self.assertEqual(Event.objects.count(), 3)
        self.assertEqual(Price.objects.count(), 3)

    @patch('scrappers.management.commands.ticketmaster.urlopen', return_value=api_response_mock)
    def test_skip_existing_records(self, urlopen_mock):
        event = Event(id='1AyZA-7GkdE1hoj')
        event.save()
        call_command('ticketmaster', **{'pages': 1})
        self.assertEqual(Event.objects.count(), 3)
        self.assertEqual(Price.objects.count(), 2)
