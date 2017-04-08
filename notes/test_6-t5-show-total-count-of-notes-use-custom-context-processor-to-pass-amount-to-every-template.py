import datetime
from unittest.mock import patch, MagicMock

from django.test import TestCase
from django.test import RequestFactory 
from django.core.urlresolvers import reverse
from notes.models import Notes
from notes.forms import NotesForm
from notes.views import CreateNotes
from django.core.files import File


class ContextProcessorTestCase(TestCase):

    def setUp(self):
        self.notes_count = Notes.objects.count()

    def test_count(self):
        resp = self.client.get(reverse('notes:requests'))
        resp2 = self.client.get(reverse('notes:create_notes'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['all_notes'], self.notes_count)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(resp2.context['all_notes'], self.notes_count)

