from django import template


register = template.Library()


@register.inclusion_tag('notes/notes.html')
def show_notes(notes):
    """Custom templatetag that process notelist from templates."""

    return {'notes': notes}

