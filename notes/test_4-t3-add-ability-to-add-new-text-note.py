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

    def test_valid_data(self):
        """Test form valid data."""

        file_mock = MagicMock(spec=File, name='FileMock')
        form = NotesForm({
            'name': "Test notes for all",
            'body': "Hi there. Thist is the test note",
            'image': file_mock,
            })
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        """Test blank data validation error"""

        form = NotesForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'body': ['This field is required.'],
            })

    def test_note_size_error(self):
        """Test if the size of a note name and body is too short"""

        short_name = 'Hi!'
        short_body = 'There!'
        form = NotesForm({
            'name': short_name,
            'body': short_body,
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': 
            ['Ensure this value has at least 10 characters (it has %s).'%len(short_name)],
            'body': ['Ensure this value has at least 10 characters (it has %s).'%len(short_body)]
            })



class NotesCreateTestCase(TestCase):
    """Tests Create View."""

    def setUp(self):
        self.form = NotesForm() 
        self.factory = RequestFactory()

    def test_get(self):
        """Test get method of the view."""

        request = self.factory.get(reverse('notes:create_notes'))
        resp = CreateNotes.as_view()(request)
        self.assertEqual(resp.status_code, 200)

    @patch('notes.models.Notes.save', MagicMock(name="save"))
    def test_post(self):
        """Test get method of the view."""

        file_mock = MagicMock(spec=File, name='FileMock')
        data = {
                'name': 'The note test',
                'body': 'This is the note test',
                'file': file_mock, 
                }

        request = self.factory.post(
                reverse('notes:create_notes'), data, 
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        resp = CreateNotes.as_view()(request)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Notes.save.called)
        self.assertEqual(Notes.save.call_count, 1)

