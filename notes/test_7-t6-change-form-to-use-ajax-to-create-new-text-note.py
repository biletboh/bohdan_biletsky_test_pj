import datetime
from unittest.mock import patch, MagicMock
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import RequestFactory
from notes.models import Notes
from notes.forms import NotesForm
from notes.views import CreateNotes
from django.core.files import File


class NotesFormTestCase(TestCase):
    """Test file form field in Notes Create Form."""

    def test_valid_data(self):
        file_mock = MagicMock(spec=File, name='FileMock')
        form = NotesForm({
            'name': "Test notes for all",
            'body': "Hi there. Thist is the test note",
            'image': file_mock,
            })
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = NotesForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'body': ['This field is required.'],
            })


class NotesCreateTestCase(TestCase):
    """The view that creates notes via ajax calls."""

    def setUp(self):
        self.form = NotesForm()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('notes:create_notes'))
        resp = CreateNotes.as_view()(request)
        self.assertEqual(resp.status_code, 200)

    @patch('notes.models.Notes.save', MagicMock(name="save"))
    def test_post(self):
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

