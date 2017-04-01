import datetime
from django.test import TestCase
from notes.models import Notes


class NotesModelTestCase(TestCase):

    def test_string_representation(self):
        note = Notes(name="Test Note")
        self.assertEqual(str(note), note.name)


class NotesViewsTestCase(TestCase):

    def test_index(self):
        fixtures = ['first_notes.json']
        note_1 = Notes.objects.create(
                name="first note",
                body="This is the test for the notes",
                pub_date=datetime.datetime.now())
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('notes_list' in resp.context)
        self.assertEqual([notes.pk for notes in resp.context['notes_list']], [1])



