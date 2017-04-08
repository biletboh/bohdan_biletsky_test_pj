import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from notes.models import Notes

class RequestListTestCase(TestCase):
    """Basic test for request list fuctionality."""

    def setUp(self):
        pass

    def test_index(self):
        resp = self.client.get(reverse('notes:requests'))
        self.assertEqual(resp.status_code, 200)

