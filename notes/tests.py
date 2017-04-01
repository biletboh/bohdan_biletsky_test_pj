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

    def setUp(self):
        self.note = Notes.objects.create(name='Test form note', body='This is the body of test form note') 

    def test_form(self):
        NotesForm(note=self.note)

    def test_init_without_entry(self):
        with self.assertRaises(KeyError):
            NotesForm()

    def test_valid_data(self):
        form = NotesForm({
            'name': "Test note",
            'body': "Hi there",
            })
    self.assertTrue(form.is_valid())
    note = form.save()
    self.assertEqual(comment.name, "Test note")
    self.assertEqual(comment.body, "Hi there")
    
    def test_blank_data(self):
        form = NotesForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['required'],
            'body': ['required'],
            })

        
class NotesCreateTestCase(TestCase):

    def setUp(self):
        self.request = HttpRequest()
        self.form = NotesForm() 

    def test_create(self):
        resp = self.client.get('/create')
        self.assertEqual(resp.status_code, 200)



