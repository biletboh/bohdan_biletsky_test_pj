from notes.models import Notes


def notes_count_processor(request):
    """Render the count of all notes."""

    notes = Notes.objects            
    return {'all_notes': notes.count()}

