import datetime
from django.test import TestCase
from notes.models import Notes
from notes.forms import NotesForm


class NotesModelTestCase(TestCase):

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
        self.assertEqual([notes.pk for notes in resp.context['notes_list']], [1])


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

    def test_create(self):
        resp = self.client.get('/create')
        self.assertEqual(resp.status_code, 200)



