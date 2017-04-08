import datetime
import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from notes.models import Notes
from django.core import serializers
from django.http import JsonResponse


class WidgetTestCase(TestCase):

    def setUp(self):
        note_1 = Notes.objects.create(
                name="first note",
                body="This is the test for the notes",
                pub_date=datetime.datetime.now())

        note_2 = Notes.objects.create(
                name="second note",
                body="This is the test for the notes",
                pub_date=datetime.datetime.now())

    def test_widget(self):
        notes = Notes.objects.all()
        notes_json = serializers.serialize('json', notes) 
        resp = self.client.get(reverse('notes:widget'))
        self.assertEqual(resp.status_code, 200)
        content = resp.content.decode('utf-8')
        json_content = json.loads(content)
        self.assertTrue(json_content[1:-1] in notes_json)

