from django import template


register = template.Library()

@register.inclusion_tag('notes/notes.html')
def show_notes(notes):
    return {'notes': notes}
