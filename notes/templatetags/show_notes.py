from django import template
from notes.models import Notes


register = template.Library()


@register.inclusion_tag('notes/notes.html')
def show_notes(note_id):
    note = Notes.objects.get(pk=note_id)
    print(note, note_id)
    return {'note': note}
