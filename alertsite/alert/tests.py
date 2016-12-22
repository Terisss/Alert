import datetime

from django.test import TestCase
from .models import Event
from django.utils import timezone
# Create your tests here.


class EventMethodsTest(TestCase):

    def test_new_event(self):
        time = timezone.now() + datetime.timedelta(days=5)
        new_event = Event(event_time=time)
        self.assertEqual(new_event.is_active(), True)

    def test_old_event(self):
        time = timezone.now() - datetime.timedelta(days=5)
        old_event = Event(event_time=time)
        self.assertEqual(old_event.is_active(), False)
