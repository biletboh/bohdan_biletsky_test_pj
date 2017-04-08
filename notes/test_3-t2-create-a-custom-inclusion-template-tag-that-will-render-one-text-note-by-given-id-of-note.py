import datetime
from django.test import TestCase
from django.template import Context, Template
from notes.models import Notes
from notes.views import NotesList


class TemplateTagsTestCase(TestCase):        
    """Test Custom inclusion tempate tag that renders one text note."""

    def setUp(self):    
        self.note_1 = Notes.objects.create(
                name="first note",
                body="This is the test for the notes",
                pub_date=datetime.datetime.now())

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context) 
    
    def test_template_tag(self):
        tag_rendered = self.render_template(
            '{%load show_notes%}'
            '{%show_notes 1%}'
            )
        
        context_rendered = self.render_template(
            '{%include "notes/notes.html"%}',
            context={'note': self.note_1}
            )

        self.assertEqual(tag_rendered, context_rendered) 

