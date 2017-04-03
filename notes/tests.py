import datetime
from unittest.mock import patch, MagicMock
from django.urls import reverse
from django.test import TestCase
from django.test import RequestFactory 
from notes.models import Notes
from notes.models import Upper 
from notes.forms import NotesForm
from notes.forms import UpperForm 
from notes.views import CreateNotes


class UpperCaseModelTestCase(TestCase):

    def test_string_representation(self):
        value = 'Test UpPercaSe' 
        note = Upper.objects.create(name=value)
        self.assertEqual(value.upper(), note.name)
    
    def test_upper_form(self):
        form_data = {'name': 'something'}
        form = UpperForm(data=form_data)
        self.assertTrue(form.is_valid())



class UpperModelTestCase(TestCase):

    def test_string_representation(self):
        note = Notes(name="Test Note")
        self.assertEqual(str(note), note.name)


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


class NotesFormTestCase(TestCase):

    def test_valid_data(self):
        form = NotesForm({
            'name': "Test notes for all",
            'body': "Hi there. Thist is the test note",
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

    def setUp(self):
        self.form = NotesForm() 
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('notes:create_notes'))
        resp = CreateNotes.as_view()(request)
        self.assertEqual(resp.status_code, 200)

    @patch('notes.models.Notes.save', MagicMock(name="save"))
    def test_post(self):
        data = {
                'name': 'The note test',
                'body': 'This is the note test'
                }

        request = self.factory.post(
                reverse('notes:create_notes'), data, 
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        resp = CreateNotes.as_view()(request)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Notes.save.called)
        self.assertEqual(Notes.save.call_count, 1)


#class NotesUpdateTestCase(TestCase):

#class NotesDeleteTestCase(TestCase):

