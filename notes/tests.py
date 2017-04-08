import datetime
from unittest.mock import patch, MagicMock

from django.test import TestCase
from django.test import RequestFactory 
from django.core.urlresolvers import reverse
from notes.models import Notes
from notes.forms import NotesForm
from notes.views import CreateNotes
from django.core.files import File


class NotesListTestCase(TestCase):

    def setUp(self):
        fixtures = ['first_notes.json']
        note_1 = Notes.objects.create(
                name="first note",
                body="This is the test for the notes",
                pub_date=datetime.datetime.now())

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('notes_list' in resp.context)
        self.assertEqual(
                [notes.pk for notes in resp.context['notes_list']], [1])


class RequestListTestCase(TestCase):

    def setUp(self):
        pass

    def test_index(self):
        resp = self.client.get(reverse('notes:requests'))
        self.assertEqual(resp.status_code, 200)
#        self.assertTrue('request_list' in resp.context)


# class NotesUpdateTestCase(TestCase):


# class NotesDeleteTestCase(TestCase):

