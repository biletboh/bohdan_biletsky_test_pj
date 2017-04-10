from django.test import TestCase
from channels import Channel
from channels.test import ChannelTestCase

class MyTests(ChannelTestCase):
    def test_a_thing(self):
    # This goes onto an in-memory channel, not the real backend.
    Channel("some-channel-name").send({"foo": "bar"})

