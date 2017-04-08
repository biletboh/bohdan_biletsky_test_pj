import datetime
from unittest.mock import patch
from django.test import TestCase
from django.core.urlresolvers import reverse
from notes.models import Notes
from notes.models import Books 
from django.db.models.signals import pre_delete, post_delete


class SignalsTestCase(TestCase):

    def setUp(self):
        note_1 = Notes.objects.create(
                name="first note",
                body="This is the test for the notes",
                pub_date=datetime.datetime.now())

        note_2 = Notes.objects.create(
                name="second note",
                body="This is the test for the notes",
                pub_date=datetime.datetime.now())
        book_1 = Books.objects.create(name="new book")
        book_1.notes.add(note_1)
        book_1.notes.add(note_2)
        book_1.save()

    def test_signal(self):
        
        with patch(
            'notes.signals.delete_empty_books', 
            autospec=True) as mocked_handler:
            pre_delete.connect(mocked_handler, sender=Notes)

            notes = Notes.objects.all()
            for note in notes:
                note.delete()

        self.assertTrue(mocked_handler.call_count, 1)
        
