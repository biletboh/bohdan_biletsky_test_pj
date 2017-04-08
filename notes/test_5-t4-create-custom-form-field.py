import datetime
from unittest.mock import patch, MagicMock

from django.test import TestCase
from django.test import RequestFactory 
from django.core.urlresolvers import reverse
from notes.models import Notes
from notes.forms import NotesForm
from notes.views import CreateNotes
from django.core.files import File


class NotesFormTestCase(TestCase):

    def test_uppercase(self):
        """Test form valid data."""

        file_mock = MagicMock(spec=File, name='FileMock')
        name = "Test notes for all"
        form = NotesForm({
            'name': name,
            'body': "Hi there. Thist is the test note",
            'image': file_mock,
            })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['name'], name.upper())

